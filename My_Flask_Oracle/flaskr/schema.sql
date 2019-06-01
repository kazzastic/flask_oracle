CREATE TABLE usee(
   ID   INT              NOT NULL,
   NAME VARCHAR (90)     NOT NULL,
   PASSWORD VARCHAR(90)  NOT NULL,    
   PRIMARY KEY (ID)
)
CREATE TABLE post(
  id    INT              NOT NUll,
  author_id INT          NOT NULL,
  title VARCHAR(10)     NOT NULL,
  body VARCHAR(10)      NOT NULL,
  FOREIGN KEY(author_id) REFERENCES use(id)
)