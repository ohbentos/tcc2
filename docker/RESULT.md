0-9 cores:
    select * from graph_view where p1=20 LIMIT 1;
    Time: 4700,879 ms (00:04,701)

    select * from graph_view where p1=20 LIMIT 10;
    Time: 46329,810 ms (00:46,330)

    select * from graph_view where p1=20 LIMIT 100;
    Time: 463764,191 ms (07:43,764)

1 core:
    select * from graph_view where p1=20 LIMIT 1;
    Time: 5362,743 ms (00:05,363)

    select * from graph_view where p1=20 LIMIT 10;
    Time: 54714,018 ms (00:54,714)


2 core:
    select * from graph_view where p1=20 LIMIT 1;
    Time: 5607,061 ms (00:05,607)

    select * from graph_view where p1=20 LIMIT 10;
    Time: 51471,219 ms (00:51,471)

3 core:
    select * from graph_view where p1=20 LIMIT 1;
    Time: 6543,276 ms (00:06,543)

    select * from graph_view where p1=20 LIMIT 10;
    Time: 54150,260 ms (00:54,150)
    
4 core:
    select * from graph_view where p1=20 LIMIT 1;
    Time: 5359,925 ms (00:05,360)

    select * from graph_view where p1=20 LIMIT 10;
    Time: 53477,425 ms (00:53,477)
