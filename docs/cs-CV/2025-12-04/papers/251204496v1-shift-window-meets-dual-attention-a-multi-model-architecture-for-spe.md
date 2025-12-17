---
layout: default
title: Shift-Window Meets Dual Attention: A Multi-Model Architecture for Specular Highlight Removal
---

# Shift-Window Meets Dual Attention: A Multi-Model Architecture for Specular Highlight Removal

**arXiv**: [2512.04496v1](https://arxiv.org/abs/2512.04496) | [PDF](https://arxiv.org/pdf/2512.04496.pdf)

**作者**: Tianci Huo, Lingfeng Qi, Yuhan Chen, Qihong Xue, Jinyuan Shao, Hai Yu, Jie Li, Zhanhua Zhang, Guofa Li

---

## 💡 一句话要点

**提出多模型架构MM-SHR以解决不同尺度高光去除问题**

**关键词**: `高光去除` `多模型架构` `卷积神经网络` `注意力机制` `长程依赖建模` `表面材料处理`

## 📋 核心要点

1. 核心问题：单模型难以兼顾局部细节与全局依赖，影响多尺度高光去除效果。
2. 方法要点：结合卷积与注意力机制，浅层提取局部细节，深层捕获全局特征，并引入OAIBlock和HDDAConv模块。
3. 实验或效果：在三个基准任务和六种表面材料上验证，MM-SHR在准确性和效率上优于现有方法。

## 📄 摘要（原文）

> Inevitable specular highlights in practical environments severely impair the visual performance, thus degrading the task effectiveness and efficiency. Although there exist considerable methods that focus on local information from convolutional neural network models or global information from transformer models, the single-type model falls into a modeling dilemma between local fine-grained details and global long-range dependencies, thus deteriorating for specular highlights with different scales. Therefore, to accommodate specular highlights of all scales, we propose a multi-model architecture for specular highlight removal (MM-SHR) that effectively captures fine-grained features in highlight regions and models long-range dependencies between highlight and highlight-free areas. Specifically, we employ convolution operations to extract local details in the shallow layers of MM-SHR, and utilize the attention mechanism to capture global features in the deep layers, ensuring both operation efficiency and removal accuracy. To model long-range dependencies without compromising computational complexity, we utilize a coarse-to-fine manner and propose Omni-Directional Attention Integration Block(OAIBlock) and Adaptive Region-Aware Hybrid-Domain Dual Attention Convolutional Network(HDDAConv) , which leverage omni-directiona pixel-shifting and window-dividing operations at the raw features to achieve specular highlight removal. Extensive experimental results on three benchmark tasks and six types of surface materials demonstrate that MM-SHR outperforms state-of-the-art methods in both accuracy and efficiency for specular highlight removal. The implementation will be made publicly available at https://github.com/Htcicv/MM-SHR.

