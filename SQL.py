# BankingApp adında database olmalı: "dbname=BankingApp user=postgres password=1234"

import psycopg2

com = """CREATE TABLE IF NOT EXISTS public.admin
(
    admin_id integer NOT NULL,
    admin_password character varying(30) COLLATE pg_catalog."default",
    CONSTRAINT "Admin_pkey" PRIMARY KEY (admin_id)
);

CREATE TABLE IF NOT EXISTS public.all_transactions
(
    customer_id integer,
    transaction_amount integer,
    transaction_type character varying(30),
    receiver_sender_id character varying(30),
    transaction_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.balance
(
    customer_id integer NOT NULL,
    current_balance integer NOT NULL,
    update_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.customer
(
    cs_name character varying(20) COLLATE pg_catalog."default",
    cs_email character varying(30) COLLATE pg_catalog."default",
    cs_password character varying(30) COLLATE pg_catalog."default",
    cs_opening_balance integer,
    bank_id integer DEFAULT 1234,
    customer_id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 12340000 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    creation_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "Customer_pkey3" PRIMARY KEY (customer_id)
);


ALTER TABLE IF EXISTS public.all_transactions
    ADD CONSTRAINT customer_id FOREIGN KEY (customer_id)
    REFERENCES public.customer (customer_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.balance
    ADD CONSTRAINT customer_id FOREIGN KEY (customer_id)
    REFERENCES public.customer (customer_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
    
CREATE INDEX IF NOT EXISTS "Balance_pkey"
    ON public.balance(customer_id)"""


conn = psycopg2.connect("dbname=BankingApp user = postgres password=1234")
cur = conn.cursor() 
cur.execute(com)
cur.execute("INSERT INTO admin VALUES(%s,%s)",(1,1))
cur.close()
conn.commit()
conn.close()