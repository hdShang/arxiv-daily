---
layout: default
title: DAP: A Discrete-token Autoregressive Planner for Autonomous Driving
---

# DAP: A Discrete-token Autoregressive Planner for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13306" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13306v1</a>
  <a href="https://arxiv.org/pdf/2511.13306.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13306v1" onclick="toggleFavorite(this, '2511.13306v1', 'DAP: A Discrete-token Autoregressive Planner for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bowen Ye, Bin Zhang, Hang Zhao

**分类**: cs.AI, cs.CV

**发布日期**: 2025-11-17

---

## 💡 一句话要点

**DAP：一种用于自动驾驶的离散token自回归规划器，实现BEV语义和轨迹联合预测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自动驾驶` `运动规划` `自回归模型` `BEV语义` `强化学习`

## 📋 核心要点

1. 现有自回归模型在自动驾驶规划中仅预测自车轨迹，存在监督信号稀疏，场景理解不足的问题。
2. DAP通过联合预测BEV语义和自车轨迹，利用场景动态信息更有效地指导自车运动规划。
3. DAP采用离散token自回归框架，并结合强化学习微调，在保证性能的同时，模型参数量较小。

## 📝 摘要（中文）

在自动驾驶领域，如何通过扩展数据和模型规模来获得可持续的性能提升仍然是一个关键但尚未解决的挑战。虽然自回归模型在规划任务中表现出令人鼓舞的数据扩展效率，但仅预测自车轨迹存在监督稀疏的问题，并且对场景演变如何影响自车运动的约束较弱。因此，我们提出了DAP，一种离散token自回归规划器，它联合预测BEV语义和自车轨迹，从而加强了全面的表征学习，并允许预测的动态直接影响自车运动。此外，我们结合了基于强化学习的微调，保留了监督行为克隆的先验知识，同时注入了奖励引导的改进。尽管参数量仅为1.6亿，DAP在open-loop指标上实现了最先进的性能，并在NAVSIM基准测试中提供了具有竞争力的closed-loop结果。总而言之，完全离散token的自回归公式在栅格化的BEV和自车动作上运行，为自动驾驶提供了一种紧凑但可扩展的规划范例。

## 🔬 方法详解

**问题定义**：自动驾驶规划需要根据周围环境预测车辆的未来轨迹。现有方法，特别是仅预测自车轨迹的自回归模型，面临监督信号稀疏的问题，难以充分利用场景信息来指导规划。此外，如何有效地利用大规模数据和模型来提升规划性能仍然是一个挑战。

**核心思路**：DAP的核心思路是联合预测BEV语义和自车轨迹，从而将场景理解和运动规划紧密结合。通过预测BEV语义，模型可以学习到更丰富的场景表征，并利用这些表征来更好地预测自车轨迹。此外，DAP采用离散token自回归框架，可以更有效地利用大规模数据进行训练。

**技术框架**：DAP的整体框架是一个离散token自回归模型。该模型接收BEV图像作为输入，并预测离散的BEV语义token和自车动作token。模型包括一个编码器，用于提取BEV图像的特征；一个自回归解码器，用于预测token序列；以及一个强化学习微调模块，用于进一步提升性能。

**关键创新**：DAP的关键创新在于联合预测BEV语义和自车轨迹，以及采用离散token自回归框架。联合预测可以增强场景理解和运动规划之间的联系，而离散token自回归框架可以更有效地利用大规模数据。此外，DAP还结合了强化学习微调，进一步提升了性能。

**关键设计**：DAP使用Transformer作为自回归解码器的基本模块。BEV图像被编码成一系列token，然后输入到Transformer解码器中。解码器预测离散的BEV语义token和自车动作token。损失函数包括交叉熵损失，用于训练BEV语义预测和自车动作预测，以及强化学习奖励，用于微调模型。

## 📊 实验亮点

DAP在NAVSIM基准测试中取得了具有竞争力的closed-loop结果，并在open-loop指标上实现了最先进的性能，超过了现有方法。值得注意的是，DAP仅使用了1.6亿参数，表明其具有较高的参数效率。实验结果表明，联合预测BEV语义和自车轨迹可以有效地提升自动驾驶规划性能。

## 🎯 应用场景

DAP可应用于各种自动驾驶场景，例如城市道路、高速公路和停车场。它可以用于车辆的路径规划、行为决策和运动控制。该研究的成果有助于提高自动驾驶系统的安全性、可靠性和效率，并为未来的自动驾驶技术发展奠定基础。

## 📄 摘要（原文）

> Gaining sustainable performance improvement with scaling data and model budget remains a pivotal yet unresolved challenge in autonomous driving. While autoregressive models exhibited promising data-scaling efficiency in planning tasks, predicting ego trajectories alone suffers sparse supervision and weakly constrains how scene evolution should shape ego motion. Therefore, we introduce DAP, a discrete-token autoregressive planner that jointly forecasts BEV semantics and ego trajectories, thereby enforcing comprehensive representation learning and allowing predicted dynamics to directly condition ego motion. In addition, we incorporate a reinforcement-learning-based fine-tuning, which preserves supervised behavior cloning priors while injecting reward-guided improvements. Despite a compact 160M parameter budget, DAP achieves state-of-the-art performance on open-loop metrics and delivers competitive closed-loop results on the NAVSIM benchmark. Overall, the fully discrete-token autoregressive formulation operating on both rasterized BEV and ego actions provides a compact yet scalable planning paradigm for autonomous driving.

