SELECT s.id as "StoryID", 
	s.title as "Title", 
	a.name as "Author 1", 
	s.ao3url as "AO3 URL", 
	replace(replace(replace(s.ao3url, "://archiveofourown.org/works/", ""), "https", "http"), "http", "") as "AO3 id",
	concat("$$TEMP SITE BASE URL$$", cast(c.id as char)) as "URL Imported From", 
	"" as "Original URL"
FROM od_sgf.$$PREFIX$$_stories s 
	join od_sgf.$$PREFIX$$_chapters c on c.storyid=s.id 
	join od_sgf.$$PREFIX$$_authors a on s.authorid=a.id
where c.position=0 or c.position=1;

