CREATE TABLE use(
   ID   INT              NOT NULL,
   NAME VARCHAR (20)     NOT NULL,
   PASSWORD VARCHAR(10)  NOT NULL,    
   PRIMARY KEY (ID)
)
CREATE TABLE post(
  id    INT              NOT NUll,
  author_id INT          NOT NULL,
  title VARCHAR(10)     NOT NULL,
  body VARCHAR(10)      NOT NULL,
  FOREIGN KEY(author_id) REFERENCES use(id)
)