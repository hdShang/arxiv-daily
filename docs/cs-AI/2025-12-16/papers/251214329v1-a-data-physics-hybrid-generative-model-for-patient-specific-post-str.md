---
layout: default
title: A data-physics hybrid generative model for patient-specific post-stroke motor rehabilitation using wearable sensor data
---

# A data-physics hybrid generative model for patient-specific post-stroke motor rehabilitation using wearable sensor data

**arXiv**: [2512.14329v1](https://arxiv.org/abs/2512.14329) | [PDF](https://arxiv.org/pdf/2512.14329.pdf)

**作者**: Yanning Dai, Chenyu Tang, Ruizhi Zhang, Wenyu Yang, Yilan Zhang, Yuhui Wang, Junliang Chen, Xuhang Chen, Ruimou Xie, Yangyue Cao, Qiaoying Li, Jin Cao, Tao Li, Hubin Zhao, Yu Pan, Arokia Nathan, Xin Gao, Peter Smielewski, Shuo Gao

**分类**: cs.CE, cs.AI

**发布日期**: 2025-12-16

**备注**: 26 pages, 6 figures

---

## 💡 一句话要点

**提出数据-物理混合生成模型，基于单次平地行走数据预测中风患者个性化康复任务中的步态，以增强临床决策。**

**关键词**: `中风康复` `步态预测` `数据-物理混合模型` `可穿戴传感器` `深度强化学习` `个性化医疗` `生成对抗模仿学习` `运动控制`

## 📋 核心要点

1. 核心问题：现有中风康复评估仅提供静态损伤评分，无法动态预测患者执行特定任务（如斜坡行走）的能力，限制了康复个性化。
2. 方法要点：结合可穿戴传感器数据、物理控制器、健康运动图谱和深度强化学习，构建混合生成模型，从单次行走数据重建个性化神经肌肉控制。
3. 实验或效果：在11名患者中提升步态模拟保真度，多中心试点显示使用预测指导康复可显著提高下肢功能评分增益。

## 📝 摘要（中文）

中风后运动能力的动态预测对于定制康复至关重要，但当前评估仅提供静态损伤评分，无法指示患者是否能安全执行特定任务，如斜坡行走或爬楼梯。本文开发了一个数据-物理混合生成框架，通过单次20米平地行走试验重建个体中风幸存者的神经肌肉控制，并预测康复场景中的任务条件化运动。该系统结合了可穿戴传感器运动学、比例-微分物理控制器、健康人群运动图谱，以及基于目标条件深度强化学习与行为克隆和生成对抗模仿学习，生成物理合理、患者特定的斜坡和楼梯步态模拟。在11名中风幸存者中，个性化控制器保留了独特步态模式，同时将关节角度和端点保真度分别提高了4.73%和12.10%，并将训练时间减少到仅物理基线的25.56%。在一项涉及21名住院患者的多中心试点中，使用我们的运动预测指导任务选择和难度的临床医生，在28天标准康复期间获得的Fugl-Meyer下肢评分增益大于对照组临床医生（平均变化6.0分对3.7分）。这些发现表明，我们的生成性任务预测框架可以增强中风后步态康复的临床决策，并为动态个性化运动恢复策略提供模板。

## 🔬 方法详解

论文提出一个数据-物理混合生成框架，整体架构整合可穿戴传感器采集的运动学数据、比例-微分物理控制器模拟生物力学约束、健康人群运动图谱作为参考基准，以及目标条件深度强化学习结合行为克隆和生成对抗模仿学习来生成任务特定步态。关键技术创新在于融合数据驱动与物理模型，实现从单次行走试验快速重建个性化控制器，并预测多种康复场景下的运动。与现有纯物理或纯数据方法相比，该方法在保持患者独特步态模式的同时，提高了模拟的物理合理性和效率。

## 📊 实验亮点

在11名中风患者中，个性化控制器将关节角度和端点保真度分别提升4.73%和12.10%，训练时间减少至基线25.56%；多中心试点中，使用预测指导康复的临床医生组下肢功能评分平均增益达6.0分，显著高于对照组的3.7分。

## 🎯 应用场景

该研究主要应用于中风后运动康复领域，通过个性化步态预测辅助临床医生制定动态康复计划，如选择安全任务（斜坡、楼梯行走）和调整难度，提升康复效果和效率，具有推动精准医疗和智能康复系统的潜力。

## 📄 摘要（原文）

> Dynamic prediction of locomotor capacity after stroke is crucial for tailoring rehabilitation, yet current assessments provide only static impairment scores and do not indicate whether patients can safely perform specific tasks such as slope walking or stair climbing. Here, we develop a data-physics hybrid generative framework that reconstructs an individual stroke survivor's neuromuscular control from a single 20 m level-ground walking trial and predicts task-conditioned locomotion across rehabilitation scenarios. The system combines wearable-sensor kinematics, a proportional-derivative physics controller, a population Healthy Motion Atlas, and goal-conditioned deep reinforcement learning with behaviour cloning and generative adversarial imitation learning to generate physically plausible, patient-specific gait simulations for slopes and stairs. In 11 stroke survivors, the personalized controllers preserved idiosyncratic gait patterns while improving joint-angle and endpoint fidelity by 4.73% and 12.10%, respectively, and reducing training time to 25.56% relative to a physics-only baseline. In a multicentre pilot involving 21 inpatients, clinicians who used our locomotion predictions to guide task selection and difficulty obtained larger gains in Fugl-Meyer lower-extremity scores over 28 days of standard rehabilitation than control clinicians (mean change 6.0 versus 3.7 points). These findings indicate that our generative, task-predictive framework can augment clinical decision-making in post-stroke gait rehabilitation and provide a template for dynamically personalized motor recovery strategies.

