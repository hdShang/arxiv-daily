---
layout: default
title: UltraDP: Generalizable Carotid Ultrasound Scanning with Force-Aware Diffusion Policy
---

# UltraDP: Generalizable Carotid Ultrasound Scanning with Force-Aware Diffusion Policy

**arXiv**: [2511.15550v1](https://arxiv.org/abs/2511.15550) | [PDF](https://arxiv.org/pdf/2511.15550.pdf)

**作者**: Ruoqu Chen, Xiangjie Yan, Kangchen Lv, Gao Huang, Zheng Li, Xiang Li

---

## 💡 一句话要点

**提出UltraDP方法以解决自主颈动脉超声扫描中的泛化性问题**

**关键词**: `自主超声扫描` `扩散策略` `多感官输入` `力-阻抗控制` `颈动脉成像`

## 📋 核心要点

1. 核心问题：患者解剖变异和复杂人机交互限制自主超声扫描的泛化性和数据利用效率
2. 方法要点：基于扩散策略接收多感官输入，结合专用引导模块和混合力-阻抗控制器
3. 实验或效果：在未见受试者上实现95%横向扫描成功率，使用大规模数据集训练

## 📄 摘要（原文）

> Ultrasound scanning is a critical imaging technique for real-time, non-invasive diagnostics. However, variations in patient anatomy and complex human-in-the-loop interactions pose significant challenges for autonomous robotic scanning. Existing ultrasound scanning robots are commonly limited to relatively low generalization and inefficient data utilization. To overcome these limitations, we present UltraDP, a Diffusion-Policy-based method that receives multi-sensory inputs (ultrasound images, wrist camera images, contact wrench, and probe pose) and generates actions that are fit for multi-modal action distributions in autonomous ultrasound scanning of carotid artery. We propose a specialized guidance module to enable the policy to output actions that center the artery in ultrasound images. To ensure stable contact and safe interaction between the robot and the human subject, a hybrid force-impedance controller is utilized to drive the robot to track such trajectories. Also, we have built a large-scale training dataset for carotid scanning comprising 210 scans with 460k sample pairs from 21 volunteers of both genders. By exploring our guidance module and DP's strong generalization ability, UltraDP achieves a 95% success rate in transverse scanning on previously unseen subjects, demonstrating its effectiveness.

