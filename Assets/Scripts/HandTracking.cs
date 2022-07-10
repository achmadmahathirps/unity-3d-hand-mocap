using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HandTracking : MonoBehaviour
{
    // Start is called before the first frame update
    public UDPReceive udpReceive;
    public GameObject[] handPoints;

    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // Retrieve UDP data
        string data = udpReceive.data;

        // Remove square brackets in the data
        data = data.Remove(0, 1);
        data = data.Remove(data.Length - 1, 1);

        // Parse the data
        string[] points = data.Split(',');

        // Send the data to the hand points
        for (int i = 0; i < 21; i++)
        {
            float x = 7 - float.Parse(points[i * 3]) / 50;
            float y = float.Parse(points[i * 3 + 1]) / 50;
            float z = float.Parse(points[i * 3 + 2]) / 25;

            handPoints[i].transform.localPosition = new Vector3(x, y, z);
        }
    }
}
