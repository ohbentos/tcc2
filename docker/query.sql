select count(*) from edges JOIN props on props.graph_id = edges.graph_id JOIN vertices on vertices.graph_id = edges.graph_id ;
