---
layout: default
title: Design and Koopman Model Predictive Control of A Soft Exoskeleton Based on Origami-Inspired Pneumatic Actuator for Knee Rehabilitation
---

# Design and Koopman Model Predictive Control of A Soft Exoskeleton Based on Origami-Inspired Pneumatic Actuator for Knee Rehabilitation

**arXiv**: [2510.11094v1](https://arxiv.org/abs/2510.11094) | [PDF](https://arxiv.org/pdf/2510.11094.pdf)

**作者**: Junxiang Wang, Han Zhang, Zehao Wang, Huaiyuan Chen, Pu Wang, Weidong Chen

---

## 💡 一句话要点

**提出基于折纸气动执行器的软外骨骼及Koopman模型预测控制，用于膝关节康复。**

**关键词**: `软外骨骼` `Koopman模型` `模型预测控制` `膝关节康复` `气动执行器` `人机交互`

## 📋 核心要点

1. 核心问题：软外骨骼人机交互动态复杂非线性，控制困难。
2. 方法要点：使用深度Koopman网络建模动态，结合肌电信号和PWM占空比输入。
3. 实验或效果：个性化模型优于非个性化，控制框架在被动和主动训练中超越PID。

## 📄 摘要（原文）

> Effective rehabilitation methods are essential for the recovery of lower limb
> dysfunction caused by stroke. Nowadays, robotic exoskeletons have shown great
> potentials in rehabilitation. Nevertheless, traditional rigid exoskeletons are
> usually heavy and need a lot of work to help the patients to put them on.
> Moreover, it also requires extra compliance control to guarantee the safety. In
> contrast, soft exoskeletons are easy and comfortable to wear and have intrinsic
> compliance, but their complex nonlinear human-robot interaction dynamics would
> pose significant challenges for control. In this work, based on the pneumatic
> actuators inspired by origami, we design a rehabilitation exoskeleton for knee
> that is easy and comfortable to wear. To guarantee the control performance and
> enable a nice human-robot interaction, we first use Deep Koopman Network to
> model the human-robot interaction dynamics. In particular, by viewing the
> electromyography (EMG) signals and the duty cycle of the PWM wave that controls
> the pneumatic robot's valves and pump as the inputs, the linear Koopman model
> accurately captures the complex human-robot interaction dynamics. Next, based
> on the obtained Koopman model, we further use Model Predictive Control (MPC) to
> control the soft robot and help the user to do rehabilitation training in
> real-time. The goal of the rehabilitation training is to track a given
> reference signal shown on the screen. Experiments show that by integrating the
> EMG signals into the Koopman model, we have improved the model accuracy to
> great extent. In addition, a personalized Koopman model trained from the
> individual's own data performs better than the non-personalized model.
> Consequently, our control framework outperforms the traditional PID control in
> both passive and active training modes. Hence the proposed method provides a
> new control framework for soft rehabilitation robots.

