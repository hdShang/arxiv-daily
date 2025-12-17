---
layout: default
title: IFG: Internet-Scale Guidance for Functional Grasping Generation
---

# IFG: Internet-Scale Guidance for Functional Grasping Generation

**arXiv**: [2511.09558v1](https://arxiv.org/abs/2511.09558) | [PDF](https://arxiv.org/pdf/2511.09558.pdf)

**作者**: Ray Muxin Liu, Mingxuan Li, Kenneth Shaw, Deepak Pathak

---

## 💡 一句话要点

**提出IFG方法，结合互联网规模语义理解与模拟几何精度，实现高性能语义抓取。**

**关键词**: `语义抓取` `力闭合抓取` `扩散模型` `点云处理` `模拟蒸馏`

## 📋 核心要点

1. 核心问题：大型视觉模型缺乏几何理解，无法精确控制灵巧手进行3D抓取。
2. 方法要点：利用模拟和力闭合抓取生成管道，蒸馏数据到扩散模型实时处理点云。
3. 实验或效果：实现高性能语义抓取，无需手动收集训练数据。

## 📄 摘要（原文）

> Large Vision Models trained on internet-scale data have demonstrated strong capabilities in segmenting and semantically understanding object parts, even in cluttered, crowded scenes. However, while these models can direct a robot toward the general region of an object, they lack the geometric understanding required to precisely control dexterous robotic hands for 3D grasping. To overcome this, our key insight is to leverage simulation with a force-closure grasping generation pipeline that understands local geometries of the hand and object in the scene. Because this pipeline is slow and requires ground-truth observations, the resulting data is distilled into a diffusion model that operates in real-time on camera point clouds. By combining the global semantic understanding of internet-scale models with the geometric precision of a simulation-based locally-aware force-closure, \our achieves high-performance semantic grasping without any manually collected training data. For visualizations of this please visit our website at https://ifgrasping.github.io/

