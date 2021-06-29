#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-06-29 11:07:16
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


import boto3


def main():
    photo="usu_p_avatar.jpg"
    bucket="bexil-rekognition-1"

    label_count = detect_labels(photo, bucket)

    print(f"Labels detected: {str(label_count)}")


def detect_labels(photo, bucket):
    client = boto3.client("rekognition")

    response = client.detect_labels(Image={
        "S3Object": {"Bucket": bucket, "Name": photo}
    }, MaxLabels=10)

    print(f"Detected labels for {photo} \n")

    for label in response["Labels"]:
        print(f"Label: {label['Name']}")
        print(f"Confidence: {str(label['Confidence'])}")
        print("Instances: ")
        
        for instance in label["Instances"]:
            print(" Bounding box")
            print(f"    Top: {str(instance['BoundingBox']['Top'])}")
            print(f"    Left: {str(instance['BoundingBox']['Left'])}")
            print(f"    Width: {str(instance['BoundingBox']['Width'])}")
            print(f"    Height: {str(instance['BoundingBox']['Height'])}")
            print(f" Confidence: {str(instance['Confidence'])}\n")
        
        print("Parents:")
        for parent in label["Parents"]:
            print(f"   {parent['Name']}")
        
        print("-------------\n")
    
    return len(response["Labels"])




if __name__ == "__main__":
    main()