FROM apache/hive:4.0.1

USER root

ADD https://jdbc.postgresql.org/download/postgresql-42.7.5.jar /opt/hive/lib/postgresql-42.7.5.jar
ADD https://jdbc.postgresql.org/download/postgresql-42.7.5.jar /opt/hadoop/share/hadoop/common/lib/postgresql-42.7.5.jar

RUN chmod 644 /opt/hive/lib/postgresql-42.7.5.jar /opt/hadoop/share/hadoop/common/lib/postgresql-42.7.5.jar

USER hive
