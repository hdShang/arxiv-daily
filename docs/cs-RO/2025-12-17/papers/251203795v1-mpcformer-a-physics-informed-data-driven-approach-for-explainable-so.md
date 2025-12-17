---
layout: default
title: MPCFormer: A physics-informed data-driven approach for explainable socially-aware autonomous driving
---

# MPCFormer: A physics-informed data-driven approach for explainable socially-aware autonomous driving

**arXiv**: [2512.03795v1](https://arxiv.org/abs/2512.03795) | [PDF](https://arxiv.org/pdf/2512.03795.pdf)

**作者**: Jia Hu, Zhexi Lian, Xuerun Yan, Ruiang Bi, Dou Shen, Yu Ruan, Haoran Wang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-03

**备注**: 17 pages, 18 figures

---

## 💡 一句话要点

**MPCFormer：基于物理信息与数据驱动的可解释社会感知自动驾驶方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `自动驾驶` `社会交互` `运动规划` `模型预测控制` `Transformer网络`

## 📋 核心要点

1. 自动驾驶车辆在高度动态和交互式的交通场景中难以表现出类人的行为，主要挑战在于缺乏对社会交互底层机制的理解。
2. MPCFormer通过耦合物理信息和数据驱动的社会交互动力学，显式建模多车辆社会交互，并利用MPC框架保证安全性。
3. 实验表明，MPCFormer在轨迹预测精度、规划成功率、驾驶效率和安全性方面均优于现有方法，尤其是在复杂交互场景中。

## 📝 摘要（中文）

本文提出了一种名为MPCFormer的可解释社会感知自动驾驶方法，该方法结合了物理信息与数据驱动的社会交互动力学。该模型将动力学公式化为离散状态空间表示，嵌入物理先验以增强模型的可解释性。动力学系数通过基于Transformer的编码器-解码器架构从自然驾驶数据中学习。据我们所知，MPCFormer是第一个显式建模多车辆社会交互动力学的方法。学习到的社会交互动力学使规划器能够在与周围交通交互时生成多样化、类人的行为。通过利用MPC框架，该方法减轻了纯粹基于学习的方法可能存在的安全风险。在NGSIM数据集上的开环评估表明，MPCFormer实现了卓越的社会交互感知，与其他最先进的方法相比，产生了最低的轨迹预测误差，在5秒的长预测范围内实现了低至0.86米的ADE。在需要连续变道的复杂交互场景中的闭环实验进一步验证了MPCFormer的有效性。结果表明，MPCFormer实现了94.67%的最高规划成功率，提高了15.75%的驾驶效率，并将碰撞率从21.25%降低到0.5%，优于基于强化学习的先进规划器。

## 🔬 方法详解

**问题定义**：现有自动驾驶系统在复杂交通场景中，尤其是在需要与其他车辆进行频繁交互的场景下，难以表现出像人类驾驶员一样的自然和社会化的行为。这主要是因为现有方法缺乏对多车辆之间社会交互动力学的有效建模，导致规划出的轨迹不够合理，甚至存在安全隐患。

**核心思路**：MPCFormer的核心思路是将物理信息融入到数据驱动的学习框架中，从而实现对社会交互动力学的可解释建模。具体来说，它首先将车辆的动力学过程表示为离散状态空间形式，并嵌入物理先验知识，然后利用Transformer网络从真实驾驶数据中学习动力学系数。这种结合物理先验和数据驱动的方法，既保证了模型的可解释性，又提高了模型的泛化能力。

**技术框架**：MPCFormer的整体框架包括三个主要模块：数据收集与预处理模块、基于Transformer的动力学学习模块和社会感知运动规划模块。首先，从自然驾驶数据集中收集车辆的运动轨迹数据，并进行预处理。然后，利用Transformer网络学习车辆之间的社会交互动力学模型。最后，将学习到的动力学模型嵌入到MPC框架中，进行社会感知的运动规划。

**关键创新**：MPCFormer最关键的创新在于它显式地建模了多车辆之间的社会交互动力学。与以往的方法不同，MPCFormer不仅考虑了车辆自身的运动状态，还考虑了周围车辆对其运动的影响。此外，MPCFormer还结合了物理信息和数据驱动的方法，从而提高了模型的可解释性和泛化能力。

**关键设计**：在动力学学习模块中，MPCFormer采用了基于Transformer的编码器-解码器结构。编码器用于提取车辆运动轨迹的特征，解码器用于预测未来的运动轨迹。损失函数包括轨迹预测误差和正则化项，用于约束模型的复杂度。在MPC框架中，采用了二次规划求解器，用于优化车辆的运动轨迹。

## 📊 实验亮点

MPCFormer在NGSIM数据集上取得了显著的性能提升。在开环轨迹预测任务中，MPCFormer的ADE（平均位移误差）低至0.86米，优于其他state-of-the-art方法。在闭环仿真实验中，MPCFormer实现了94.67%的规划成功率，提高了15.75%的驾驶效率，并将碰撞率从21.25%降低到0.5%，显著优于基于强化学习的规划器。

## 🎯 应用场景

MPCFormer的研究成果可应用于各种自动驾驶场景，尤其是在城市交通、高速公路等复杂环境中。通过提高自动驾驶车辆的社会感知能力和交互能力，可以提升交通效率、降低事故率，并改善乘客的乘坐体验。此外，该方法还可以为高级驾驶辅助系统（ADAS）提供更智能的决策支持。

## 📄 摘要（原文）

> Autonomous Driving (AD) vehicles still struggle to exhibit human-like behavior in highly dynamic and interactive traffic scenarios. The key challenge lies in AD's limited ability to interact with surrounding vehicles, largely due to a lack of understanding the underlying mechanisms of social interaction. To address this issue, we introduce MPCFormer, an explainable socially-aware autonomous driving approach with physics-informed and data-driven coupled social interaction dynamics. In this model, the dynamics are formulated into a discrete space-state representation, which embeds physics priors to enhance modeling explainability. The dynamics coefficients are learned from naturalistic driving data via a Transformer-based encoder-decoder architecture. To the best of our knowledge, MPCFormer is the first approach to explicitly model the dynamics of multi-vehicle social interactions. The learned social interaction dynamics enable the planner to generate manifold, human-like behaviors when interacting with surrounding traffic. By leveraging the MPC framework, the approach mitigates the potential safety risks typically associated with purely learning-based methods. Open-looped evaluation on NGSIM dataset demonstrates that MPCFormer achieves superior social interaction awareness, yielding the lowest trajectory prediction errors compared with other state-of-the-art approach. The prediction achieves an ADE as low as 0.86 m over a long prediction horizon of 5 seconds. Close-looped experiments in highly intense interaction scenarios, where consecutive lane changes are required to exit an off-ramp, further validate the effectiveness of MPCFormer. Results show that MPCFormer achieves the highest planning success rate of 94.67%, improves driving efficiency by 15.75%, and reduces the collision rate from 21.25% to 0.5%, outperforming a frontier Reinforcement Learning (RL) based planner.

