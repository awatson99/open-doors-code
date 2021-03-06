# encoding: utf-8
import csv

import sys

from shared_python import Args
from shared_python.Sql import Sql
from shared_python.Tags import Tags

if __name__ == "__main__":
  """
  When Tag Wrangling have finished mapping the tags in Google Drive, export the spreadsheet as a CSV file. This script
  then copies the AO3 tags from that file into the tags table in the temporary database.
  """
  args = Args.args_for_04()
  sql = Sql(args)
  tags = Tags(args, sql.db)

  with open(args.tag_input_file, 'r') as csvfile:
    tw_tags = list(csv.DictReader(csvfile))
    tag_headers = tags.tag_export_map
    total = len(tw_tags)

    for cur, row in enumerate(tw_tags):
      sys.stdout.write('\r{0}/{1} tags to map'.format(cur + 1, total))
      sys.stdout.flush()

      prefix = 'fanfiction' if args.archive_type == 'EF' else None
      tags.update_tag_row(row, prefix)

  print('\n')
