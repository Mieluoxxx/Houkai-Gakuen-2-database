## 安装
```bash
brew install postgresql@15
```
- 连接数据库
```bash
psql -h localhost -p 5432 -U postgres moguw
```

- 修改密码
```
psql 
\password moguw
```

- 建表
```bash
create table person(
    id bigserial not null primary key,
    name varchar(200) not null,
    gender varchar(7) not null,
    birthday date not null,
    email varchar(250)
);
```

- 插入与查询
```bash
select name from person;

insert into person(name, gender, birthday)values('moguw', 'male', '2003-02-01');
```

- mock数据
[生成假数据](https://www.mockaroo.com)

- 限制
```bash
select * from person limit 10;
```

- 忽略
```bash
select * from person offset 5 limit 5;
```

- 修改表结构
```bash	
alter table person add column VIP bit not null default B'0';
```
- 添加主键
```bash
alter table person add primary key(id);
```

- 修改数据
```bash
update person set id = id-1000;
```

## 可能遇到的问题
```bash
psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: server closed the connection unexpectedly
	This probably means the server terminated abnormally
	before or while processing the request.
# 解决方法
rm /opt/homebrew/var/postgresql@15/postmaster.pid
vim /opt/homebrew/var/postgresql@15/postmaster.conf
# 将端口5432的注释取消
```

```bash
psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: FATAL:  database "xxx" does not exist
# 解决方法
createdb xxx
```


