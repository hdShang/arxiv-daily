---
layout: default
title: "WoW: Towards a World omniscient World model Through Embodied Interaction"
---

# WoW: Towards a World omniscient World model Through Embodied Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22642" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22642v2</a>
  <a href="https://arxiv.org/pdf/2509.22642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22642v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22642v2', 'WoW: Towards a World omniscient World model Through Embodied Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaowei Chi, Peidong Jia, Chun-Kai Fan, Xiaozhu Ju, Weishi Mi, Kevin Zhang, Zhiyuan Qin, Wanxin Tian, Kuangzhi Ge, Hao Li, Zezhong Qian, Anthony Chen, Qiang Zhou, Yueru Jia, Jiaming Liu, Yong Dai, Qingpo Wuwu, Chengyu Bai, Yu-Kai Wang, Ying Li, Lizhang Chen, Yong Bao, Zhiyuan Jiang, Jiacheng Zhu, Kai Tang, Ruichuan An, Yulin Luo, Qiuxuan Feng, Siyuan Zhou, Chi-min Chan, Chengkai Hou, Wei Xue, Sirui Han, Yike Guo, Shanghang Zhang, Jian Tang

**分类**: cs.RO, cs.CV, cs.MM

**发布日期**: 2025-09-26 (更新: 2025-10-16)

---

## 💡 一句话要点

**WoW：通过具身交互构建具备物理直觉的世界模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `具身智能` `物理直觉` `机器人交互` `生成式模型`

## 📋 核心要点

1. 现有视频模型依赖被动观察，难以理解物理因果关系，阻碍了对世界的深入理解。
2. WoW通过大规模机器人交互学习，构建生成式世界模型，提升对物理世界的理解能力。
3. WoW在物理一致性和因果推理基准上表现出色，验证了具身交互对发展物理直觉的重要性。

## 📝 摘要（中文）

本文提出了WoW，一个基于2百万机器人交互轨迹训练的140亿参数生成式世界模型，旨在解决当前视频模型（如Sora）在理解物理因果关系方面的不足。研究表明，WoW对物理的理解是基于对合理结果的概率分布，这可能导致随机不稳定性和物理幻觉。为了约束模型向物理真实性靠拢，引入了SOPHIA，利用视觉-语言模型评估DiT生成的输出，并通过迭代演化语言指令来指导改进。此外，共同训练的逆动力学模型将这些改进的计划转化为可执行的机器人动作，从而闭合了从想象到行动的循环。WoW在WoWBench（一个关注视频中物理一致性和因果推理的新基准）上取得了最先进的性能，证明了其在物理因果关系、碰撞动力学和物体永存方面的强大能力。该研究系统地证明了大规模真实世界交互是发展人工智能物理直觉的基石。模型、数据和基准将开源。

## 🔬 方法详解

**问题定义**：当前视频生成模型，例如Sora，主要依赖于被动观察学习，缺乏与真实世界的交互，因此在理解物理世界的因果关系方面存在不足，容易产生不符合物理规律的幻觉。论文旨在通过让AI模型与真实世界进行大规模交互，从而学习到更真实的物理直觉。

**核心思路**：论文的核心思路是通过大规模的机器人交互数据训练一个生成式世界模型（WoW），使其能够像人类一样通过与环境的交互来学习物理规律。此外，引入SOPHIA框架，利用视觉-语言模型对生成结果进行评估和指导，从而约束模型向物理真实性靠拢。

**技术框架**：整体框架包含三个主要模块：1) **WoW (World Model)**：一个基于扩散Transformer (DiT) 的生成式世界模型，通过2百万机器人交互轨迹进行训练。2) **SOPHIA (Self-Refinement with Physical Intuition Augmentation)**：利用视觉-语言模型评估WoW生成的视频，并生成语言指令来指导WoW进行改进。3) **Inverse Dynamics Model (IDM)**：一个逆动力学模型，将SOPHIA生成的改进计划转化为可执行的机器人动作，从而实现从想象到行动的闭环。

**关键创新**：该论文的关键创新在于：1) 强调了大规模真实世界交互对于发展AI物理直觉的重要性，并构建了相应的训练框架。2) 提出了SOPHIA框架，利用视觉-语言模型对生成结果进行物理一致性评估和指导，从而有效提升了生成视频的物理真实性。3) 构建了WoWBench，一个新的用于评估视频中物理一致性和因果推理能力的基准。

**关键设计**：WoW模型基于扩散Transformer (DiT) 架构，使用大规模机器人交互数据进行训练。SOPHIA框架使用预训练的视觉-语言模型（具体模型未知）来评估生成视频的物理合理性，并生成自然语言指令来指导模型进行改进。逆动力学模型（IDM）的具体结构和训练方法未知。损失函数的设计也未知。

## 📊 实验亮点

WoW在WoWBench基准测试中取得了最先进的性能，证明了其在物理因果关系、碰撞动力学和物体永存方面的强大能力。通过人类和自主评估，WoW在物理一致性和因果推理方面均优于现有方法。具体的性能数据和提升幅度在摘要中未明确给出，需要参考论文正文。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动驾驶、游戏AI等领域。通过让AI模型具备更强的物理直觉，可以提升机器人在复杂环境中的适应性和决策能力，例如，在未知环境中进行导航和操作，或在虚拟环境中创建更逼真的物理交互效果。未来，该研究有望推动通用人工智能的发展，使AI能够更好地理解和适应真实世界。

## 📄 摘要（原文）

> Humans develop an understanding of intuitive physics through active interaction with the world. This approach is in stark contrast to current video models, such as Sora, which rely on passive observation and therefore struggle with grasping physical causality. This observation leads to our central hypothesis: authentic physical intuition of the world model must be grounded in extensive, causally rich interactions with the real world. To test this hypothesis, we present WoW, a 14-billion-parameter generative world model trained on 2 million robot interaction trajectories. Our findings reveal that the model's understanding of physics is a probabilistic distribution of plausible outcomes, leading to stochastic instabilities and physical hallucinations. Furthermore, we demonstrate that this emergent capability can be actively constrained toward physical realism by SOPHIA, where vision-language model agents evaluate the DiT-generated output and guide its refinement by iteratively evolving the language instructions. In addition, a co-trained Inverse Dynamics Model translates these refined plans into executable robotic actions, thus closing the imagination-to-action loop. We establish WoWBench, a new benchmark focused on physical consistency and causal reasoning in video, where WoW achieves state-of-the-art performance in both human and autonomous evaluation, demonstrating strong ability in physical causality, collision dynamics, and object permanence. Our work provides systematic evidence that large-scale, real-world interaction is a cornerstone for developing physical intuition in AI. Models, data, and benchmarks will be open-sourced.

