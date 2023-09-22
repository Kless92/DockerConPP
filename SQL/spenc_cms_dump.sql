--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

-- Started on 2023-09-22 18:26:42 UTC

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
-- TOC entry 214 (class 1259 OID 19714)
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
-- TOC entry 213 (class 1259 OID 19713)
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
-- TOC entry 3363 (class 0 OID 0)
-- Dependencies: 213
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- TOC entry 217 (class 1259 OID 19731)
-- Name: courses_professors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses_professors (
    course_id integer NOT NULL,
    professor_id integer NOT NULL
);


ALTER TABLE public.courses_professors OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 19723)
-- Name: professors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professors (
    id integer NOT NULL,
    name text NOT NULL,
    useraccount_id integer NOT NULL
);


ALTER TABLE public.professors OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 19722)
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
-- TOC entry 3364 (class 0 OID 0)
-- Dependencies: 215
-- Name: professors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.professors_id_seq OWNED BY public.professors.id;


--
-- TOC entry 212 (class 1259 OID 19705)
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
-- TOC entry 211 (class 1259 OID 19704)
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
-- TOC entry 3365 (class 0 OID 0)
-- Dependencies: 211
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- TOC entry 210 (class 1259 OID 19692)
-- Name: useraccounts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.useraccounts (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    email text,
    user_status text
);


ALTER TABLE public.useraccounts OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 19691)
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
-- TOC entry 3366 (class 0 OID 0)
-- Dependencies: 209
-- Name: useraccounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.useraccounts_id_seq OWNED BY public.useraccounts.id;


--
-- TOC entry 3187 (class 2604 OID 19717)
-- Name: courses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- TOC entry 3188 (class 2604 OID 19726)
-- Name: professors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors ALTER COLUMN id SET DEFAULT nextval('public.professors_id_seq'::regclass);


--
-- TOC entry 3186 (class 2604 OID 19708)
-- Name: students id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- TOC entry 3185 (class 2604 OID 19695)
-- Name: useraccounts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts ALTER COLUMN id SET DEFAULT nextval('public.useraccounts_id_seq'::regclass);


--
-- TOC entry 3354 (class 0 OID 19714)
-- Dependencies: 214
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (id, name, start_date, end_date) FROM stdin;
1	History of Europe	2024-01-15 10:00:00	2024-05-22 11:30:00
2	Art Appreciation	2024-01-15 14:30:00	2024-05-22 16:00:00
3	Advance Physics	2024-01-16 09:00:00	2024-05-24 10:30:00
4	Advance Chemistry	2024-01-15 10:00:00	2024-05-21 11:30:00
7	Egnlish II	2024-01-15 08:30:00	2024-05-24 10:00:00
10	Python IV	2024-01-18 09:00:00	2024-05-23 13:00:00
11	History of Aferica	2024-06-01 11:00:00	2024-10-25 12:00:00
\.


--
-- TOC entry 3357 (class 0 OID 19731)
-- Dependencies: 217
-- Data for Name: courses_professors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses_professors (course_id, professor_id) FROM stdin;
1	4
3	2
4	3
7	1
\.


--
-- TOC entry 3356 (class 0 OID 19723)
-- Dependencies: 216
-- Data for Name: professors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.professors (id, name, useraccount_id) FROM stdin;
2	Cathie	5
3	Edith	8
1	Andy	1
12	Mario	2
4	Goddie	4
\.


--
-- TOC entry 3352 (class 0 OID 19705)
-- Dependencies: 212
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.students (id, name, useraccount_id, course_id) FROM stdin;
5	Hanna	7	7
2	Rob	5	4
6	Dexter	1	4
11	DeeDee	23	4
3	Mobbie	2	4
4	Fionna	3	11
\.


--
-- TOC entry 3350 (class 0 OID 19692)
-- Dependencies: 210
-- Data for Name: useraccounts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.useraccounts (id, username, password, email, user_status) FROM stdin;
4	dogDude	doggie	dog@gmail.com	professor
5	mcDe	1234	kfc@gamil.com	professor
2	BubbleBass	5678	bass@gmail.com	student
3	catzzz	kitten	\N	student
6	JohnyK	9999	\N	student
8	Lyla	6798133ae3193ca600e9bbddf680787ab40778ffe1722285e4dd9fc40bc522117392758c9033b250ff9061efc2623701098b1d0b3c390a7f3faa96f61c8b1be6	lyla@st.edu	professor
18	Cider	b87be9c60640595f9cd0189aa7a275708fba404ee069981c98b1e021889d4d5fd1a402b75346d281017fcdf984431f1f7eb5df1e5c888a67af2520391d7de2ec	app@pia.com	professor
7	Zimmermen	996c1e37ec79b2cbb19bf0e933438493aaddec15914538638d070b44487995225b47533d6ea2ea41757ef54903f74ad43e780378a7ec83b496b34fbfdeb2f6d1	zim@AAA.org	professor
23	zelda	f2f56a74e65bd9b47c26df3eb6dba34c8b776fb0848e4b0bfa7d07ba7b4ad90a3d8a2b279a13bf2320ca26e65e936cb11e261410f702dd99302f53fbd46cbb5e	tri@hy.com	professor
1	Apple Jack	1234	apple@kellogg.com	professor
\.


--
-- TOC entry 3367 (class 0 OID 0)
-- Dependencies: 213
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.courses_id_seq', 11, true);


--
-- TOC entry 3368 (class 0 OID 0)
-- Dependencies: 215
-- Name: professors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.professors_id_seq', 12, true);


--
-- TOC entry 3369 (class 0 OID 0)
-- Dependencies: 211
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.students_id_seq', 11, true);


--
-- TOC entry 3370 (class 0 OID 0)
-- Dependencies: 209
-- Name: useraccounts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.useraccounts_id_seq', 25, true);


--
-- TOC entry 3198 (class 2606 OID 19721)
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);


--
-- TOC entry 3204 (class 2606 OID 19735)
-- Name: courses_professors courses_professors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses_professors
    ADD CONSTRAINT courses_professors_pkey PRIMARY KEY (course_id, professor_id);


--
-- TOC entry 3200 (class 2606 OID 19730)
-- Name: professors professors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_pkey PRIMARY KEY (id);


--
-- TOC entry 3202 (class 2606 OID 28103)
-- Name: professors professors_useraccount_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT professors_useraccount_id_key UNIQUE (useraccount_id);


--
-- TOC entry 3196 (class 2606 OID 19712)
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- TOC entry 3190 (class 2606 OID 19703)
-- Name: useraccounts useraccounts_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts
    ADD CONSTRAINT useraccounts_email_key UNIQUE (email);


--
-- TOC entry 3192 (class 2606 OID 19699)
-- Name: useraccounts useraccounts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts
    ADD CONSTRAINT useraccounts_pkey PRIMARY KEY (id);


--
-- TOC entry 3194 (class 2606 OID 19701)
-- Name: useraccounts useraccounts_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.useraccounts
    ADD CONSTRAINT useraccounts_username_key UNIQUE (username);


--
-- TOC entry 3208 (class 2606 OID 19746)
-- Name: courses_professors fk_course_professors_courses; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses_professors
    ADD CONSTRAINT fk_course_professors_courses FOREIGN KEY (course_id) REFERENCES public.courses(id);


--
-- TOC entry 3209 (class 2606 OID 19751)
-- Name: courses_professors fk_course_professors_professors; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses_professors
    ADD CONSTRAINT fk_course_professors_professors FOREIGN KEY (professor_id) REFERENCES public.professors(id);


--
-- TOC entry 3207 (class 2606 OID 19756)
-- Name: professors fk_professors_useraccounts; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professors
    ADD CONSTRAINT fk_professors_useraccounts FOREIGN KEY (useraccount_id) REFERENCES public.useraccounts(id);


--
-- TOC entry 3206 (class 2606 OID 19741)
-- Name: students fk_students_courses; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT fk_students_courses FOREIGN KEY (course_id) REFERENCES public.courses(id);


--
-- TOC entry 3205 (class 2606 OID 19736)
-- Name: students fk_students_useraccounts; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT fk_students_useraccounts FOREIGN KEY (useraccount_id) REFERENCES public.useraccounts(id);


-- Completed on 2023-09-22 18:26:43 UTC

--
-- PostgreSQL database dump complete
--

