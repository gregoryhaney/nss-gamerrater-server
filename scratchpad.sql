-- Top five games by rating
SELECT r.rating, g.description
FROM raterprojectapi_rating AS r
JOIN raterprojectapi_game AS g
    ON r.game_id = g.id
ORDER BY r.rating ASC
LIMIT 5



-- Bottom five games by rating
SELECT  r.rating, 
        g.description,
        g.title
FROM raterprojectapi_rating AS r
JOIN raterprojectapi_game AS g
    ON r.game_id = g.id
ORDER BY r.rating DESC
LIMIT 5


-- Nbr of games in each category
SELECT  c.cat_name AS Category, 
        g.description AS GameDescription,
        COUNT(g.id) AS NbrGames
FROM raterprojectapi_game AS g
JOIN raterprojectapi_category AS c
    ON c.id = g.id
GROUP BY Category


-- Which games can have >5 players
SELECT  g.description AS GameDescription, 
        g.number_of_players AS NbrPlayers
FROM raterprojectapi_game AS g
WHERE g.number_of_players > 5


-- What is the most-reviewed game
SELECT  g.description AS Game, 
        COUNT(r.id) AS Count
FROM raterprojectapi_review AS r
JOIN raterprojectapi_game AS g
ON r.game_id = g.id
GROUP BY r.id


-- Who is player w/ most games added
-- to the collection
SELECT  gr.handle AS Gamer,
        COUNT(g.id)
FROM raterprojectapi_game AS g
JOIN raterprojectapi_gamer AS gr
ON g.gamer_id = gr.id
GROUP BY gr.handle


-- What are the games of any category
-- that are suitable for age < 8
SELECT  g.description,
        g.age_rec AS Age
FROM raterprojectapi_game AS g
WHERE g.age_rec < 8


-- How many games do not have pictures
SELECT  COUNT(g.id)
FROM raterprojectapi_game AS g
LEFT JOIN raterprojectapi_image AS i
    ON g.id = i.game_id        
WHERE i.url is NULL       
 

-- By count, who are the top three
-- game reviewers
SELECT  gr.handle AS GamerHandle,
        COUNT(r.id) AS NbrReviews
FROM raterprojectapi_review AS r
JOIN raterprojectapi_gamer AS gr
ON r.gamer_id = gr.id
GROUP BY gr.handle
ORDER BY r.id DESC


