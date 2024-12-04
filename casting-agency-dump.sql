--
-- PostgreSQL database dump
--

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
-- Name: actor; Type: TABLE; Schema: public; Owner: student
--

CREATE TABLE public.actor (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    age integer NOT NULL,
    gender character varying(10) NOT NULL,
    movie_id integer
);


ALTER TABLE public.actor OWNER TO student;

--
-- Name: actor_id_seq; Type: SEQUENCE; Schema: public; Owner: student
--

CREATE SEQUENCE public.actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.actor_id_seq OWNER TO student;

--
-- Name: actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: student
--

ALTER SEQUENCE public.actor_id_seq OWNED BY public.actor.id;


--
-- Name: movie; Type: TABLE; Schema: public; Owner: student
--

CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    release_date timestamp without time zone NOT NULL
);


ALTER TABLE public.movie OWNER TO student;

--
-- Name: movie_id_seq; Type: SEQUENCE; Schema: public; Owner: student
--

CREATE SEQUENCE public.movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.movie_id_seq OWNER TO student;

--
-- Name: movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: student
--

ALTER SEQUENCE public.movie_id_seq OWNED BY public.movie.id;


--
-- Name: actor id; Type: DEFAULT; Schema: public; Owner: student
--

ALTER TABLE ONLY public.actor ALTER COLUMN id SET DEFAULT nextval('public.actor_id_seq'::regclass);


--
-- Name: movie id; Type: DEFAULT; Schema: public; Owner: student
--

ALTER TABLE ONLY public.movie ALTER COLUMN id SET DEFAULT nextval('public.movie_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: student
--

COPY public.actor (id, name, age, gender, movie_id) FROM stdin;
1	Actor 1	26	Male	1
2	Actor 2	26	Male	2
3	Actor 3	26	Male	3
4	Actor 4	20	Male	3
5	Actor 5	20	Male	2
6	Actor 6	20	Male	2
\.


--
-- Data for Name: movie; Type: TABLE DATA; Schema: public; Owner: student
--

COPY public.movie (id, title, release_date) FROM stdin;
1	Movie 1	2024-01-01 00:00:00
2	Movie 2	2024-01-01 00:00:00
3	Movie 3	2024-01-01 00:00:00
\.


--
-- Name: actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: student
--

SELECT pg_catalog.setval('public.actor_id_seq', 6, true);


--
-- Name: movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: student
--

SELECT pg_catalog.setval('public.movie_id_seq', 3, true);


--
-- Name: actor actor_pkey; Type: CONSTRAINT; Schema: public; Owner: student
--

ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (id);


--
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: student
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);


--
-- Name: actor actor_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: student
--

ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);


--
-- PostgreSQL database dump complete
--

