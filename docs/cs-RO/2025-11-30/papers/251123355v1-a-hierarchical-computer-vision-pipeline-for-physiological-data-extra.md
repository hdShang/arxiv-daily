---
layout: default
title: A Hierarchical Computer Vision Pipeline for Physiological Data Extraction from Bedside Monitors
---

# A Hierarchical Computer Vision Pipeline for Physiological Data Extraction from Bedside Monitors

**arXiv**: [2511.23355v1](https://arxiv.org/abs/2511.23355) | [PDF](https://arxiv.org/pdf/2511.23355.pdf)

**作者**: Vinh Chau, Khoa Le Dinh Van, Hon Huynh Ngoc, Binh Nguyen Thien, Hao Nguyen Thien, Vy Nguyen Quang, Phuc Vo Hong, Yen Lam Minh, Kieu Pham Tieu, Trinh Nguyen Thi Diem, Louise Thwaites, Hai Ho Bich

---

## 💡 一句话要点

**提出基于计算机视觉的层次化管道，从床边监护仪屏幕自动提取生理数据以解决低资源医疗环境的数据集成问题。**

**关键词**: `计算机视觉` `生理数据提取` `床边监护仪` `光学字符识别` `低资源医疗` `层次化检测`

## 📋 核心要点

1. 核心问题：低资源医疗环境中，床边监护仪缺乏网络连接，导致生理数据难以集成到电子健康记录系统。
2. 方法要点：采用YOLOv11进行监护仪和感兴趣区域定位，结合PaddleOCR进行文本提取，并通过几何校正模块提升鲁棒性。
3. 实验或效果：在6,498张图像数据集上评估，监护仪检测mAP@50-95达99.5%，端到端提取核心参数准确率超过98.9%。

## 📄 摘要（原文）

> In many low-resource healthcare settings, bedside monitors remain standalone legacy devices without network connectivity, creating a persistent interoperability gap that prevents seamless integration of physiological data into electronic health record (EHR) systems. To address this challenge without requiring costly hardware replacement, we present a computer vision-based pipeline for the automated capture and digitisation of vital sign data directly from bedside monitor screens. Our method employs a hierarchical detection framework combining YOLOv11 for accurate monitor and region of interest (ROI) localisation with PaddleOCR for robust text extraction. To enhance reliability across variable camera angles and lighting conditions, a geometric rectification module standardizes the screen perspective before character recognition. We evaluated the system on a dataset of 6,498 images collected from open-source corpora and real-world intensive care units in Vietnam. The model achieved a mean Average Precision (mAP@50-95) of 99.5% for monitor detection and 91.5% for vital sign ROI localisation. The end-to-end extraction accuracy exceeded 98.9% for core physiological parameters, including heart rate, oxygen saturation SpO2, and arterial blood pressure. These results demonstrate that a lightweight, camera-based approach can reliably transform unstructured information from screen captures into structured digital data, providing a practical and scalable pathway to improve information accessibility and clinical documentation in low-resource settings.

