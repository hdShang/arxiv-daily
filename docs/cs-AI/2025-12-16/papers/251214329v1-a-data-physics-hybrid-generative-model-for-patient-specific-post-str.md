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

**提出数据-物理混合生成框架，基于单次平地行走数据预测中风患者个性化康复任务中的步态模拟，以增强临床决策。**

🎯 **匹配领域**: **人形机器人** **动作生成** **视觉里程计** **强化学习**

**关键词**: `数据-物理混合模型` `个性化康复` `步态模拟` `深度强化学习` `可穿戴传感器` `中风康复` `生成对抗模仿学习` `临床决策支持`

## 📋 核心要点

1. 核心问题：现有中风康复评估仅提供静态损伤评分，无法动态预测患者执行特定任务（如斜坡行走）的能力，限制了康复方案的个性化定制。
2. 方法要点：提出数据-物理混合生成框架，结合可穿戴传感器数据、物理控制器和深度学习，从单次平地行走重建患者神经肌肉控制，并生成任务条件步态模拟。
3. 实验或效果：在11名患者中，个性化控制器提升关节角度和端点保真度，减少训练时间；多中心试点显示临床使用后患者康复评分显著提高。

## 📝 摘要（中文）

中风后运动能力的动态预测对于定制康复至关重要，但当前评估仅提供静态损伤评分，无法指示患者是否能安全执行特定任务，如斜坡行走或爬楼梯。本文开发了一个数据-物理混合生成框架，通过单次20米平地行走试验重建个体中风幸存者的神经肌肉控制，并预测康复场景中的任务条件运动。该系统结合了可穿戴传感器运动学、比例-微分物理控制器、健康人群运动图谱，以及基于目标条件的深度强化学习与行为克隆和生成对抗模仿学习，生成物理上合理、患者特定的斜坡和楼梯步态模拟。在11名中风幸存者中，个性化控制器保留了独特步态模式，同时将关节角度和端点保真度分别提高了4.73%和12.10%，并将训练时间减少到仅物理基线的25.56%。在一项涉及21名住院患者的多中心试点中，使用我们的运动预测指导任务选择和难度的临床医生，在28天标准康复期间获得的Fugl-Meyer下肢评分增益大于对照组临床医生（平均变化6.0分对3.7分）。这些发现表明，我们的生成性任务预测框架可以增强中风后步态康复的临床决策，并为动态个性化运动恢复策略提供模板。

## 🔬 方法详解

论文提出一个数据-物理混合生成框架，整体架构包括：基于可穿戴传感器采集的运动学数据，结合比例-微分物理控制器模拟生物力学约束，利用健康人群运动图谱作为参考基准，并通过目标条件深度强化学习（结合行为克隆和生成对抗模仿学习）生成个性化步态模拟。关键技术创新点在于融合数据驱动与物理模型，实现从单次平地行走数据重建患者特异性神经肌肉控制，并预测不同康复任务（如斜坡、楼梯）下的运动。与现有方法的主要区别在于，传统方法多依赖静态评估或纯物理模拟，而本框架通过混合方法提高了模拟的物理合理性和个性化程度，同时减少了数据需求和训练时间。

## 📊 实验亮点

最重要的实验结果：在11名中风患者中，个性化控制器将关节角度和端点保真度分别提升4.73%和12.10%，训练时间减少至基线25.56%；多中心试点中，使用预测的临床医生组患者Fugl-Meyer评分平均增益达6.0分，显著高于对照组的3.7分，验证了框架的临床有效性。

## 🎯 应用场景

该研究主要应用于中风后运动康复领域，潜在价值包括：为临床医生提供动态预测工具，指导个性化康复任务选择和难度调整；作为模板推广到其他神经系统疾病或运动障碍的康复策略中，提升康复效率和效果。

## 📄 摘要（原文）

> Dynamic prediction of locomotor capacity after stroke is crucial for tailoring rehabilitation, yet current assessments provide only static impairment scores and do not indicate whether patients can safely perform specific tasks such as slope walking or stair climbing. Here, we develop a data-physics hybrid generative framework that reconstructs an individual stroke survivor's neuromuscular control from a single 20 m level-ground walking trial and predicts task-conditioned locomotion across rehabilitation scenarios. The system combines wearable-sensor kinematics, a proportional-derivative physics controller, a population Healthy Motion Atlas, and goal-conditioned deep reinforcement learning with behaviour cloning and generative adversarial imitation learning to generate physically plausible, patient-specific gait simulations for slopes and stairs. In 11 stroke survivors, the personalized controllers preserved idiosyncratic gait patterns while improving joint-angle and endpoint fidelity by 4.73% and 12.10%, respectively, and reducing training time to 25.56% relative to a physics-only baseline. In a multicentre pilot involving 21 inpatients, clinicians who used our locomotion predictions to guide task selection and difficulty obtained larger gains in Fugl-Meyer lower-extremity scores over 28 days of standard rehabilitation than control clinicians (mean change 6.0 versus 3.7 points). These findings indicate that our generative, task-predictive framework can augment clinical decision-making in post-stroke gait rehabilitation and provide a template for dynamically personalized motor recovery strategies.

