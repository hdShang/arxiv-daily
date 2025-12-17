---
layout: default
title: Design and Koopman Model Predictive Control of A Soft Exoskeleton Based on Origami-Inspired Pneumatic Actuator for Knee Rehabilitation
---

# Design and Koopman Model Predictive Control of A Soft Exoskeleton Based on Origami-Inspired Pneumatic Actuator for Knee Rehabilitation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11094" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11094v1</a>
  <a href="https://arxiv.org/pdf/2510.11094.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11094v1" onclick="toggleFavorite(this, '2510.11094v1', 'Design and Koopman Model Predictive Control of A Soft Exoskeleton Based on Origami-Inspired Pneumatic Actuator for Knee Rehabilitation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junxiang Wang, Han Zhang, Zehao Wang, Huaiyuan Chen, Pu Wang, Weidong Chen

**分类**: cs.RO

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**提出基于折纸气动软体外骨骼的Koopman模型预测控制方法，用于膝关节康复。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `软体外骨骼` `膝关节康复` `Koopman模型` `模型预测控制` `肌电信号` `人机交互` `深度学习`

## 📋 核心要点

1. 传统刚性外骨骼笨重且穿戴复杂，需要额外的柔顺性控制以保证安全，而软体外骨骼虽然舒适，但其复杂的人机交互动力学难以控制。
2. 论文提出使用深度Koopman网络对人-机交互动力学进行建模，并结合模型预测控制(MPC)实现对软体外骨骼的精确控制。
3. 实验结果表明，该方法通过整合EMG信号提高了模型精度，个性化模型优于非个性化模型，且控制性能优于传统PID控制。

## 📝 摘要（中文）

本文提出了一种基于折纸气动执行器的软体外骨骼，用于膝关节康复。软体外骨骼穿戴舒适，但其复杂非线性的人-机交互动力学给控制带来了挑战。本文利用深度Koopman网络对人-机交互动力学进行建模，将肌电信号(EMG)和控制气动执行器阀门和泵的PWM波占空比作为输入，线性Koopman模型能够准确捕捉复杂的人-机交互动力学。在此基础上，采用模型预测控制(MPC)控制软体机器人，辅助用户进行实时康复训练，目标是跟踪屏幕上给定的参考信号。实验结果表明，将EMG信号融入Koopman模型能够显著提高模型精度。此外，基于个体数据训练的个性化Koopman模型优于非个性化模型。所提出的控制框架在被动和主动训练模式下均优于传统的PID控制，为软体康复机器人提供了一种新的控制框架。

## 🔬 方法详解

**问题定义**：论文旨在解决软体外骨骼在膝关节康复应用中，由于复杂非线性人-机交互动力学带来的控制难题。现有方法，如PID控制，难以有效应对这种复杂性，导致康复效果不佳。

**核心思路**：论文的核心思路是利用Koopman理论将非线性系统近似为线性系统，从而简化控制器的设计。通过深度Koopman网络学习人-机交互动力学，将复杂的非线性关系映射到高维线性空间，便于进行预测和控制。

**技术框架**：整体框架包括：1) 基于折纸气动执行器的软体外骨骼设计；2) 数据采集，包括EMG信号和PWM控制信号；3) 深度Koopman网络建模，学习人-机交互动力学；4) 基于Koopman模型的模型预测控制(MPC)；5) 实时康复训练，跟踪参考信号。

**关键创新**：最重要的技术创新点在于将深度Koopman网络应用于软体外骨骼的人-机交互动力学建模。与传统方法相比，Koopman方法能够更好地捕捉非线性系统的动态特性，并将其转化为线性系统进行分析和控制。此外，将EMG信号作为Koopman网络的输入，进一步提高了模型的精度。

**关键设计**：Koopman网络的输入包括EMG信号和PWM控制信号，输出为下一时刻的系统状态。网络结构未知，但目标是学习一个Koopman算子，将当前状态映射到高维空间，并在该空间中进行线性预测。MPC控制器基于Koopman模型进行优化，目标是最小化跟踪误差和控制输入。

## 📊 实验亮点

实验结果表明，将EMG信号融入Koopman模型能够显著提高模型精度。个性化Koopman模型优于非个性化模型，表明了个性化建模的重要性。所提出的控制框架在被动和主动训练模式下均优于传统的PID控制，验证了该方法的有效性。具体性能数据未知。

## 🎯 应用场景

该研究成果可应用于中风等引起的下肢功能障碍患者的康复训练。通过个性化的软体外骨骼和精确的控制，可以帮助患者进行更有效、更舒适的康复训练，提高康复效果。未来，该技术还可扩展到其他关节的康复，甚至应用于运动辅助和增强等领域。

## 📄 摘要（原文）

> Effective rehabilitation methods are essential for the recovery of lower limb dysfunction caused by stroke. Nowadays, robotic exoskeletons have shown great potentials in rehabilitation. Nevertheless, traditional rigid exoskeletons are usually heavy and need a lot of work to help the patients to put them on. Moreover, it also requires extra compliance control to guarantee the safety. In contrast, soft exoskeletons are easy and comfortable to wear and have intrinsic compliance, but their complex nonlinear human-robot interaction dynamics would pose significant challenges for control. In this work, based on the pneumatic actuators inspired by origami, we design a rehabilitation exoskeleton for knee that is easy and comfortable to wear. To guarantee the control performance and enable a nice human-robot interaction, we first use Deep Koopman Network to model the human-robot interaction dynamics. In particular, by viewing the electromyography (EMG) signals and the duty cycle of the PWM wave that controls the pneumatic robot's valves and pump as the inputs, the linear Koopman model accurately captures the complex human-robot interaction dynamics. Next, based on the obtained Koopman model, we further use Model Predictive Control (MPC) to control the soft robot and help the user to do rehabilitation training in real-time. The goal of the rehabilitation training is to track a given reference signal shown on the screen. Experiments show that by integrating the EMG signals into the Koopman model, we have improved the model accuracy to great extent. In addition, a personalized Koopman model trained from the individual's own data performs better than the non-personalized model. Consequently, our control framework outperforms the traditional PID control in both passive and active training modes. Hence the proposed method provides a new control framework for soft rehabilitation robots.

