# @ author sunshine
# -*- coding: UTF-8 -*-
import logging; logging.basicConfig(level=logging.INFO)
import aiomysql


async def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['sunshine'],
        password=kw['HouZhicheng#2!'],
        db=kw['outdoor_push'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

async def select(sql, args, size=None):
    log()