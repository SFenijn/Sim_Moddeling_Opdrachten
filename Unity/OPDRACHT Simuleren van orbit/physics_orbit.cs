using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class physics_orbit : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
    public Vector3 startForce;
    public Vector3 centerPoint;
    public Vector3 r;
    public float distance;
    public double Gravity;
    public int earthmass;
    public int sunMass;
    public int friction;
    public int springForce;
    public int speed;
    

    // Start is called before the first frame update
    void Start()
    {
        centerPoint = new Vector3(0, 0, 0);
        Gravity = 9.81;
        earthmass = 0;
        sunMass = 0;
        friction = 0;
        springForce = -100;

        Velocity = new Vector3(1, 1, 0);

    }

    // Update is called once per frame
    void FixedUpdate()
    {
        distance = Vector3.Distance(centerPoint, transform.position);
        r = transform.position;
        Force = -10 / Mathf.Pow(r.magnitude, 2) * (r / r.magnitude);
        Velocity += Force * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;

    }
}
