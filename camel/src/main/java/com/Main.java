package com;

import org.apache.camel.CamelContext;
import org.apache.camel.impl.DefaultCamelContext;

/* Simple Apache Camel context with a single Camel route that copies all files from
 * an input directory to an output directory every 5 minutes.
 */
public class Main {

    public static void main(String[] args) {
        SimpleRouteBuilder routeBuilder = new SimpleRouteBuilder();
        CamelContext ctx = new DefaultCamelContext();
        try {
            ctx.addRoutes(routeBuilder);
            ctx.start();
            Thread.sleep(5 * 60 * 1000);
            ctx.stop();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
