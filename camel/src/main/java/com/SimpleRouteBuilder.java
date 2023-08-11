package com;

import org.apache.camel.builder.RouteBuilder;

/* Simiple Route for copying files from one directory to another.
 */
public class SimpleRouteBuilder extends RouteBuilder {

    @Override
    public void configure() throws Exception {
        from("file:C:/inputFiles?noop=true").to("file:C:/outputFiles");
    }

}
