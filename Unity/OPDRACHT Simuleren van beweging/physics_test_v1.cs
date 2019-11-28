using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class physics_test_v1 : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
    public Vector3 startForce;
    public Vector3 Gravity;
    public int mass;
    public int friction;
    public int springForce;

    // Start is called before the first frame update
    void Start()
    {
        Gravity = new Vector3(0, 0, 0);
        mass = 10;
        friction = 5;
        springForce = -100;
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        Force = springForce * transform.position + Gravity - friction*Velocity;
        Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
        
    }
}
