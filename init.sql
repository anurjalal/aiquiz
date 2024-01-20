CREATE TABLE user (
    id int AUTO_INCREMENT NOT NULL,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(username)
);

CREATE TABLE quiz_result (
    id int AUTO_INCREMENT NOT NULL,
    username varchar(255),
    answer_id_taken int,
    is_correct boolean,
    question_id_taken int,
    PRIMARY KEY(id)
);

CREATE TABLE question (
    id int AUTO_INCREMENT NOT NULL,
    question varchar(255) NOT NULL,
    correct_answer_id int,
    PRIMARY KEY(id),
    UNIQUE(question)
);

CREATE TABLE leaderboard (
    username varchar(255) NOT NULL,
    score int,
    PRIMARY KEY(username)
);

CREATE TABLE answer (
    id int AUTO_INCREMENT NOT NULL,
    question_id int,
    answer varchar(255),
    PRIMARY KEY(id)
);


INSERT INTO question (question)
VALUES 
('Dalam machine learning, hal yang penting dari suatu input disebut'),
("Penerapan machine learning pada teks atau suara sering disebut sebagai"),
("Manakah library berikut yang digunakan untuk membuat model machine learning"),
("Berikut ini adalah salah satu contoh kegunaan AI, kecuali")


INSERT INTO answer (question_id, answer) VALUES 
(1, "label"),
(1, "fitur"),
(1, "akurasi"),
(1, "matriks"),
(2, "Natural Language Processing"),
(2, "Computer Vision"),
(2, "reinforcement learning"),
(2, "transfer learning"),
(3, "pycharm"),
(3, "IntelliJ"), 
(3, "tensorflow"),
(3, "dev c++"),
(4, "Memprediksi harga saham di masa depan"), 
(4, "rekomendasi produk pada ecommerce"), 
(4, "melakukan pekerjaan secara manual"), 
(4, "mendeteksi objek secara otomatis")


UPDATE question SET correct_answer_id= 2 WHERE id=1
UPDATE question SET correct_answer_id= 5 WHERE id=2
UPDATE question SET correct_answer_id= 11 WHERE id=3
UPDATE question SET correct_answer_id= 5 WHERE id=4;
