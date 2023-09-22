--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    id integer NOT NULL,
    name text NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- Name: courses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_id_seq OWNER TO postgres;

--
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- Name: courses_professors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses_professors (
    course_id integer NOT NULL,
    professor_id integer NOT NULL
);


ALTER TABLE public.courses_professors OWNER TO postgres;

--
-- Name: professors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professors (
    id integer NOT NULL,
    name text NOT NULL,
    useraccount_id integer NOT NULL
);


ALTER TABLE public.professors OWNER TO postgres;

--
-- Name: professors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.professors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.professors_id_seq OWNER TO postgres;

--
-- Name: professors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.professors_id_seq OWNED BY public.professors.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    id integer NOT NULL,
    name text NOT NULL,
    useraccount_id integer NOT NULL,
    course_id integer
);


ALTER TABLE public.students OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO postgres;

--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Name: useraccounts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.useraccounts (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    email text
);


ALTER TABLE public.useraccounts OWNER TO postgres;

--
-- Name: useraccounts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.useraccounts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.useraccounts_id_seq OWNER TO postgres;

--
-- Name: useraccounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.useraccounts_id_seq OWNED BY public.useraccounts.id;


--
-- Name: courses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- Name: professors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors ALTER COLUMN id SET DEFAULT nextval('public.professors_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Name: useraccounts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts ALTER COLUMN id SET DEFAULT nextval('public.useraccounts_id_seq'::regclass);


--
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (id, name, start_date, end_date) FROM stdin;
1	History of Europe	2024-01-15 10:00:00	2024-05-22 11:30:00
2	Art Appreciation	2024-01-15 14:30:00	2024-05-22 16:00:00
3	Advance Physics	2024-01-16 09:00:00	2024-05-24 10:30:00
4	Advance Chemistry	2024-01-15 10:00:00	2024-05-21 11:30:00
5	Python IV	2024-01-18 09:00:00	2024-05-23 13:00:00
6	History of Propaganda	2024-01-17 11:00:00	2024-05-22 13:30:00
7	Egnlish II	2024-01-15 08:30:00	2024-05-24 10:00:00
\.


--
-- Data for Name: courses_professors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses_professors (course_id, professor_id) FROM stdin;
1	4
3	2
4	3
7	1
\.


--
-- Data for Name: professors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.professors (id, name, useraccount_id) FROM stdin;
1	Andy	1
2	Cathie	5
3	Edith	8
4	Gob	4
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students (id, name, useraccount_id, course_id) FROM stdin;
2	Bob	2	4
3	Duge	6	1
4	Fiona	3	\N
5	Hanna	7	7
\.


--
-- Data for Name: useraccounts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.useraccounts (id, username, password, email) FROM stdin;
1	Acod	1234	a@gmail.com
2	BubbleBass	5678	bass@gmail.com
3	catzzz	kitten	\N
4	dogDude	doggie	dog@gmail.com
5	mcDe	1234	kfc@gamil.com
6	JohnyK	9999	\N
7	JandD	naughty	\N
8	lifeLover	love96	lolo@gmail.com
\.


--
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.courses_id_seq', 7, true);


--
-- Name: professors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.professors_id_seq', 4, true);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.students_id_seq', 5, true);


--
-- Name: useraccounts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.useraccounts_id_seq', 8, true);


--
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);


--
-- Name: courses_professors courses_professors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses_professors
    ADD CONSTRAINT courses_professors_pkey PRIMARY KEY (course_id, professor_id);


--
-- Name: professors professors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_pkey PRIMARY KEY (id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Name: useraccounts useraccounts_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts
    ADD CONSTRAINT useraccounts_email_key UNIQUE (email);


--
-- Name: useraccounts useraccounts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts
    ADD CONSTRAINT useraccounts_pkey PRIMARY KEY (id);


--
-- Name: useraccounts useraccounts_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts
    ADD CONSTRAINT useraccounts_username_key UNIQUE (username);


--
-- Name: courses_professors fk_course_professors_courses; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses_professors
    ADD CONSTRAINT fk_course_professors_courses FOREIGN KEY (course_id) REFERENCES public.courses(id);


--
-- Name: courses_professors fk_course_professors_professors; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses_professors
    ADD CONSTRAINT fk_course_professors_professors FOREIGN KEY (professor_id) REFERENCES public.professors(id);


--
-- Name: professors fk_professors_useraccounts; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT fk_professors_useraccounts FOREIGN KEY (useraccount_id) REFERENCES public.useraccounts(id);


--
-- Name: students fk_students_courses; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT fk_students_courses FOREIGN KEY (course_id) REFERENCES public.courses(id);


--
-- Name: students fk_students_useraccounts; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT fk_students_useraccounts FOREIGN KEY (useraccount_id) REFERENCES public.useraccounts(id);


--
-- PostgreSQL database dump complete
--

