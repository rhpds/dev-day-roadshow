package com.parasol;

import java.util.HashMap;
import java.util.Map;

import io.quarkus.logging.Log;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

@Path("/api/claims/stats")
@Produces(MediaType.APPLICATION_JSON)
public class ClaimsStatsResource {

    private final ClaimsResource claimsResource;

    public ClaimsStatsResource(ClaimsResource claimsResource) {
        this.claimsResource = claimsResource;
    }

    @GET
    public Map<String, Object> getStats() {
        Map<String, Object> stats = new HashMap<>();

        Log.info("Fetching claim statistics");

        try {
            var claims = claimsResource.getAllClaims();
            stats.put("total", claims.size());

            Map<String, Long> byCategory = new HashMap<>();
            for (var claim : claims) {
                byCategory.merge(claim.getCategory(), 1L, Long::sum);
            }
            stats.put("by_category", byCategory);

            Map<String, Long> byStatus = new HashMap<>();
            for (var claim : claims) {
                byStatus.merge(claim.getStatus(), 1L, Long::sum);
            }
            stats.put("by_status", byStatus);
        } catch (Exception e) {
            Log.error("Error fetching claim statistics", e);
        }

        return stats;
    }
}
