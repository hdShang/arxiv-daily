---
layout: default
title: MIMIC-MJX: Neuromechanical Emulation of Animal Behavior
---

# MIMIC-MJX: Neuromechanical Emulation of Animal Behavior

**arXiv**: [2511.20532v1](https://arxiv.org/abs/2511.20532) | [PDF](https://arxiv.org/pdf/2511.20532.pdf)

**作者**: Charles Y. Zhang, Yuanjia Yang, Aidan Sirbu, Elliott T. T. Abe, Emil Wärnberg, Eric J. Leonardis, Diego E. Aldarondo, Adam Lee, Aaditya Prasad, Jason Foat, Kaiwen Bian, Joshua Park, Rusham Bhatt, Hutton Saunders, Akira Nagamori, Ayesha R. Thanawalla, Kee Wui Huang, Fabian Plum, Hendrik K. Beck, Steven W. Flavell, David Labonte, Blake A. Richards, Bingni W. Brunton, Eiman Azim, Bence P. Ölveczky, Talmo D. Pereira

---

## 💡 一句话要点

**提出MIMIC-MJX框架，从运动学数据学习生物合理神经控制策略，用于神经科学研究。**

**关键词**: `神经控制策略` `生物力学模拟` `运动学学习` `物理仿真` `神经科学建模`

## 📋 核心要点

1. 核心问题：运动学轨迹无法直接揭示神经控制机制。
2. 方法要点：训练神经控制器驱动生物力学模型，在物理模拟中重现真实运动。
3. 实验或效果：框架准确、快速、数据高效，可泛化到多种动物模型。

## 📄 摘要（原文）

> The primary output of the nervous system is movement and behavior. While recent advances have democratized pose tracking during complex behavior, kinematic trajectories alone provide only indirect access to the underlying control processes. Here we present MIMIC-MJX, a framework for learning biologically-plausible neural control policies from kinematics. MIMIC-MJX models the generative process of motor control by training neural controllers that learn to actuate biomechanically-realistic body models in physics simulation to reproduce real kinematic trajectories. We demonstrate that our implementation is accurate, fast, data-efficient, and generalizable to diverse animal body models. Policies trained with MIMIC-MJX can be utilized to both analyze neural control strategies and simulate behavioral experiments, illustrating its potential as an integrative modeling framework for neuroscience.

