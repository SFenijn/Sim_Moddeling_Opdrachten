using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Physics_orbit : MonoBehaviour
{
    public float Nudge = 100;
    public Vector3 center;
    public int mass;


    //G = 6.67 * 10^-11 N.m².kg^-2
    private double G = 6.674f * (10 ^ 11);

    Rigidbody rb;
    // Start is called before the first frame update
    void Start()
    {
        mass = 100;
        center = new Vector3(0, 0, 0);
        rb = GetComponent<Rigidbody>();
        rb.AddForce(transform.right * Nudge * 10);
    }

    void FixedUpdate()
    {
        Vector3 location = rb.position;
        Vector3 velocity = rb.velocity;
        Vector3 dist = center - location;
        float r = dist.magnitude;
        dist /= r;

        float parentMass = mass;
        float force = ((float)G * mass * parentMass) / (r * r);

        rb.velocity += dist * force;
    }
}