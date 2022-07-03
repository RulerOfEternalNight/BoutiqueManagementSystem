create database BoutiqueManagementSystem;
use BoutiqueManagementSystem;

show databases;

DROP DATABASE BoutiqueManagementSystem;

create table employeeLogin(
    empUsername varchar(16) primary key,
    empPassword varchar(25)
);

create table employeeDetails(
    empid varchar(7) primary key,
    empname varchar(25),
    empUsername varchar(16) references employeeLogin(empUsername),
    emprolerank int
);

create table employeePhone(
    empid varchar(7) references employeeDetails(empid),
    empPhone numeric(10)
);

#-------------------------------------------------------------------------------------

create table customerLogin(
    userId int primary key auto_increment,
    custUserMail varchar(25) unique,
    custPassword varchar(25)
);

#-------------------------------------------------------------------------------------

create table productsmain1(
    prodid int primary key auto_increment, 
    prodname varchar(20), 
    prodtype varchar(20)
);

create table productsmain2(
    prodtype varchar(20) primary key, 
    amount float, 
    gender char
);

create table productssecondary(
    prodid int,
    qtyinstock int, 
    dresssize varchar(3), 
    dresscolor varchar(10)
);

#-------------------------------------------------------------------------------------

create table customers(
    custid int primary key auto_increment, 
    custname varchar(25),
    email varchar(25),
    houseno varchar(25),
    street varchar(25),
    pincode numeric(6)
);

create table custPhone(
    custid int references customers(custid),
    custPhone numeric(10)
);

#-------------------------------------------------------------------------------------

create table bill_1(
    custid int,
    prodid int,
    qty int,
    billid int
);

create table bill_2(
    billid int, 
    modeofpayment varchar(25),
    billdate varchar(10)
);

#-------------------------------------------------------------------------------------

create table cart(
    custid int, 
    prodid int, 
    qty int
);

#-------------------------------------------------------------------------------------

create table returnorder(
    returnid varchar(5) primary key,
    billid int,
    custid int,
    prodid int,
    retDateTime varchar(20)
);


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


insert into employeeLogin values('cb.en.u4cse20127','password127');
insert into employeeLogin values('cb.en.u4cse20102','password102');
insert into employeeLogin values('cb.en.u4cse20124','password124');
insert into employeeLogin values('cb.en.u4cse20123','password123');

insert into employeeDetails values('agej444', 'Jegadit', 'cb.en.u4cse20127', 1);
insert into employeeDetails values('riba567', 'Abiram', 'cb.en.u4cse20102', 2);
insert into employeeDetails values('irah323', 'Harish', 'cb.en.u4cse20124', 3);
insert into employeeDetails values('urug111', 'Guru', 'cb.en.u4cse20123', 3);


insert into employeePhone values('agej444', 9234567890), ('agej444', 6928301742);
insert into employeePhone values('riba567', 9087654321);
insert into employeePhone values('irah323', 9087612345);
insert into employeePhone values('urug111', 6789012345), ('urug111', 8352912738);

#/////////////////////////////////////////////////////////////////////////////////////

insert into customerLogin values(1, 'liamjohn@gmail.com', 'userpass1');
insert into customerLogin values(2, 'johnsson@yahoo.com', 'userpass2');
insert into customerLogin values(3, 'pamprimo65@outlook.com', 'userpass3');
insert into customerLogin values(4, 'colt90jessie@gmail.com', 'userpass4');
insert into customerLogin values(5, 'edgarr12@gmail.com', 'userpass5');
insert into customerLogin values(6, 'ben10@hotmail.com', 'userpass6');

#/////////////////////////////////////////////////////////////////////////////////////

insert into productsmain1 values(1,'silksaree','designersaree');
insert into productsmain1 values(2,'hi-quality salwar','salwar');
insert into productsmain1 values(3,'cotton churidhar','churidhar');
insert into productsmain1 values(4,'sherwani','readymadesherwani');
insert into productsmain1 values(5,'coat-suit','coatsuit');


insert into productsmain2 values('designersaree',2000,'F');
insert into productsmain2 values('salwar',4500,'F');
insert into productsmain2 values('churidhar',2000,'F');
insert into productsmain2 values('readymadesherwani',6000,'M');
insert into productsmain2 values('coatsuit',9000,'M');


insert into productssecondary values(1, 10, 'n/a', 'red'), (1, 5, 'n/a', 'green'), (1, 7, 'n/a', 'pink'), (1 ,15, 'n/a', 'blue');
insert into productssecondary values(2, 3, 'S', 'red'), (2, 7, 'M', 'red'), (2, 5, 'XL', 'blue');
insert into productssecondary values(3, 15, 'S', 'blue'), (3, 10, 'S', 'peach'), (3, 5, 'M', 'blue'), (3, 15, 'M', 'peach ');
insert into productssecondary values(4, 15, 'n/a', 'blue'), (4, 15, 'n/a', 'peach'), (4, 15, 'n/a', 'red');
insert into productssecondary values(5, 15, 'S', 'grey'), (5, 15, 'S', 'black'), (5, 15, 'M', 'grey'), (5, 15, 'L', 'grey');

#/////////////////////////////////////////////////////////////////////////////////////

insert into customers values (1, 'Liam John', 'liamjohn@gmail.com', 'house no 5', 'ab street', '600001');
insert into customers values (2, 'Johnsson', 'johnsson@yahoo.com', 'house no 6', 'def street', '600011');
insert into customers values (3, 'Pam Primo', 'pamprimo65@outlook.com', 'house no 7', 'ghi street', '600045');
insert into customers values (4, 'Jessie Colt', 'colt90jessie@gmail.com', 'house no 9', 'mno street', '600034');
insert into customers values (5, 'Edgar Ronald', 'edgarr12@gmail.com', 'house no 10', 'pqr street', '600067');
insert into customers values (6, 'Ben Tennyson', 'ben10@hotmail.com', 'house no 11', 'stu street', '600035');

insert into custPhone values(1, 7895645789);
insert into custPhone values(2, 9870472648);
insert into custPhone values(3, 9997254926), (3, 6009378244);
insert into custPhone values(4, 7936523764);
insert into custPhone values(5, 8987649361);
insert into custPhone values(6, 8642107247), (6, 9343275855);


#/////////////////////////////////////////////////////////////////////////////////////

insert into bill_1 values(1,4,1,90912);
insert into bill_1 values(1,5,1,90913);
insert into bill_1 values(2,2,2,90914);
insert into bill_1 values(3,3,1,90915);
insert into bill_1 values(4,1,2,90916);
insert into bill_1 values(5,4,2,90917);
insert into bill_1 values(6,5,1,90918);
insert into bill_1 values(5,3,2,90919);
insert into bill_1 values(1,5,2,90912);

insert into bill_2 values(90912,'cash','12-06-2021');
insert into bill_2 values(90913,'cash','14-07-2021');
insert into bill_2 values(90914,'cash','23-07-2021');
insert into bill_2 values(90915,'cash','02-08-2021');
insert into bill_2 values(90916,'cash','18-08-2021');
insert into bill_2 values(90917,'cash','20-08-2021');
insert into bill_2 values(90918,'cash','24-09-2021');
insert into bill_2 values(90919,'cash','01-10-2021');

#/////////////////////////////////////////////////////////////////////////////////////

insert into cart values (1, 1, 3);
insert into cart values (1, 2, 2);
insert into cart values (2, 1, 5);
insert into cart values (3, 1, 5);
insert into cart values (4, 1, 5);
insert into cart values (5, 1, 5);
insert into cart values (6, 1, 5);


#/////////////////////////////////////////////////////////////////////////////////////

insert into returnorder values ('ret1', 90912, 1, 4, '15-06-2021 : 15:38');
insert into returnorder values ('ret2', 90918, 6, 5, '16-06-2021 : 17:45');
insert into returnorder values ('ret3', 90919, 5, 3, '16-06-2021 : 18:00');


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


select * from employeeLogin;
select * from employeeDetails;
select * from employeePhone;

select * from customerLogin;

select * from productsmain1;
select * from productsmain2;
select * from productssecondary;

select * from customers;
select * from custPhone;

select * from bill_1;
select * from bill_2;

select * from cart;

select * from returnorder;



SELECT * FROM employeeDetails WHERE empId = 'agej444';
SELECT empPhone FROM employeePhone WHERE empId = 'agej444';

SET SQL_SAFE_UPDATES = 0;
DELETE FROM customers, custPhone USING customers INNER JOIN custPhone ON customers.custid = custPhone.custid  WHERE customers.custid= 6;
SET SQL_SAFE_UPDATES = 1;

select * from productsmain1 where prodid in (select prodid from bill_1 where billid = 90912);
select amount from productsmain2 where prodtype in (select prodtype from productsmain1 where prodid in (select prodid from bill_1 where billid = 90912) );
select prodname from productsmain1 where prodid in (select prodid from bill_1 where billid = 90912);

select custname from customers where custid in (select custid from returnorder);
select prodname from productsmain1 where prodid in (select prodid from returnorder);

select * from productsmain1 where prodid in (select prodid from cart where custid = 1);
select amount from productsmain2 where prodtype in (select prodtype from productsmain1 where prodid in (select prodid from cart where custid = 1));
select qty from cart where custid=1;

DELETE FROM employeeLogin, employeeDetails USING employeeLogin INNER JOIN employeeDetails ON employeeLogin.empUsername = employeeDetails.empUsername  WHERE employeeDetails.empid= 'stab333';

select max(prodid) from productssecondary;
select distinct sum(qtyinstock) from productssecondary where prodid=1;
select distinct sum(qtyinstock) from productssecondary where prodid=2;
select distinct sum(qtyinstock) from productssecondary where prodid=3;
select distinct sum(qtyinstock) from productssecondary where prodid=4;