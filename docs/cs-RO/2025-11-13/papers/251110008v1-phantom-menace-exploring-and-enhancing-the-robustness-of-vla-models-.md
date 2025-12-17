---
layout: default
title: Phantom Menace: Exploring and Enhancing the Robustness of VLA Models against Physical Sensor Attacks
---

# Phantom Menace: Exploring and Enhancing the Robustness of VLA Models against Physical Sensor Attacks

**arXiv**: [2511.10008v1](https://arxiv.org/abs/2511.10008) | [PDF](https://arxiv.org/pdf/2511.10008.pdf)

**作者**: Xuancun Lu, Jiaxiang Chen, Shilin Xiao, Zizhi Jin, Zhangrui Chen, Hanwen Yu, Bohan Qian, Ruochen Zhou, Xiaoyu Ji, Wenyuan Xu

---

## 💡 一句话要点

**提出物理传感器攻击框架与防御方法以增强VLA模型在机器人系统中的鲁棒性**

**关键词**: `VLA模型` `物理传感器攻击` `鲁棒性增强` `对抗训练` `机器人安全` `多模态集成`

## 📋 核心要点

1. 核心问题：VLA模型对物理世界传感器攻击的安全性未充分探索，存在显著漏洞。
2. 方法要点：引入Real-Sim-Real框架，模拟并验证针对摄像头和麦克风的物理攻击向量。
3. 实验或效果：通过大规模评估揭示漏洞模式，并开发基于对抗训练的防御方法提升鲁棒性。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models revolutionize robotic systems by enabling end-to-end perception-to-action pipelines that integrate multiple sensory modalities, such as visual signals processed by cameras and auditory signals captured by microphones. This multi-modality integration allows VLA models to interpret complex, real-world environments using diverse sensor data streams. Given the fact that VLA-based systems heavily rely on the sensory input, the security of VLA models against physical-world sensor attacks remains critically underexplored.
>   To address this gap, we present the first systematic study of physical sensor attacks against VLAs, quantifying the influence of sensor attacks and investigating the defenses for VLA models. We introduce a novel ``Real-Sim-Real'' framework that automatically simulates physics-based sensor attack vectors, including six attacks targeting cameras and two targeting microphones, and validates them on real robotic systems. Through large-scale evaluations across various VLA architectures and tasks under varying attack parameters, we demonstrate significant vulnerabilities, with susceptibility patterns that reveal critical dependencies on task types and model designs. We further develop an adversarial-training-based defense that enhances VLA robustness against out-of-distribution physical perturbations caused by sensor attacks while preserving model performance. Our findings expose an urgent need for standardized robustness benchmarks and mitigation strategies to secure VLA deployments in safety-critical environments.

