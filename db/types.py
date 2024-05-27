from db.mongodb import MongoDatabase

from .neo4j import Neo4jDatabase
from .postgres import PGDatabase

type Database = Neo4jDatabase | PGDatabase | MongoDatabase
