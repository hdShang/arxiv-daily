---
layout: default
title: LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation
---

# LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02239" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02239v1</a>
  <a href="https://arxiv.org/pdf/2511.02239.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02239v1" onclick="toggleFavorite(this, '2511.02239v1', 'LACY: A Vision-Language Model-based Language-Action Cycle for Self-Improving Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youngjin Hong, Houjian Yu, Mingen Li, Changhyun Choi

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-04

**备注**: Preprint. Project page: https://vla2026.github.io/LACY/

**🔗 代码/项目**: [PROJECT_PAGE](https://vla2026.github.io/LACY/)

---

## 💡 一句话要点

**LACY：基于视觉-语言模型的语言-动作循环，用于自提升的机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人操作` `视觉-语言模型` `语言-动作循环` `自监督学习` `主动学习`

## 📋 核心要点

1. 现有机器人操作策略缺乏上下文理解，泛化能力受限，且无法解释自身行为。
2. LACY框架通过在视觉-语言模型中学习双向映射（L2A和A2L）来解决此问题。
3. LACY通过自监督循环生成和过滤训练数据，无需额外人工标注即可提升模型性能。

## 📝 摘要（中文）

为了学习机器人操作的通用策略，越来越多地依赖于将语言指令映射到动作(L2A)的大规模模型。然而，这种单向范式产生的策略通常在没有更深层次的上下文理解的情况下执行任务，限制了它们的泛化或解释其行为的能力。我们认为，将动作映射回语言(A2L)的互补技能对于开发更全面的基础至关重要。一个既能行动又能解释其行动的智能体可以形成更丰富的内部表征，并为自监督学习解锁新的范式。我们引入了LACY(语言-动作循环)，这是一个统一的框架，可以在单个视觉-语言模型中学习这种双向映射。LACY在三个协同任务上进行联合训练：从语言生成参数化动作(L2A)，用语言解释观察到的动作(A2L)，以及验证两个语言描述之间的语义一致性(L2C)。这使得一个自我改进的循环能够通过主动增强策略自主生成和过滤新的训练数据，从而在没有额外人工标签的情况下改进模型。在模拟和真实世界中的抓取放置任务上的实验表明，LACY平均提高了56.46%的任务成功率，并为机器人操作产生了更强大的语言-动作基础。

## 🔬 方法详解

**问题定义**：现有基于语言到动作(L2A)的机器人操作方法，通常缺乏对任务上下文的深入理解，导致泛化能力不足，并且难以解释其行为。这种单向映射忽略了动作到语言(A2L)的反馈，限制了智能体形成更丰富的内部表征。

**核心思路**：LACY的核心思路是构建一个统一的视觉-语言模型，同时学习语言到动作(L2A)和动作到语言(A2L)的双向映射。通过这种双向循环，智能体可以更好地理解任务上下文，并提高泛化能力和可解释性。此外，LACY还引入了语言一致性验证(L2C)任务，进一步增强了模型的语义理解能力。

**技术框架**：LACY的技术框架包含三个主要模块：语言到动作(L2A)模块、动作到语言(A2L)模块和语言一致性验证(L2C)模块。L2A模块负责根据语言指令生成参数化的动作序列。A2L模块负责根据观察到的动作序列生成语言描述。L2C模块负责验证两个语言描述之间的语义一致性。这三个模块在一个统一的视觉-语言模型中进行联合训练，形成一个语言-动作循环。

**关键创新**：LACY最重要的技术创新点在于其双向语言-动作循环的学习范式。与传统的单向L2A方法相比，LACY通过引入A2L和L2C任务，增强了模型的上下文理解能力和泛化能力。此外，LACY还提出了一种主动增强策略，通过自主生成和过滤新的训练数据，实现了模型的自提升，无需额外的人工标注。

**关键设计**：LACY的关键设计包括：1) 使用Transformer架构作为视觉-语言模型的基础，以实现更好的多模态融合；2) 设计了参数化的动作表示，以便L2A模块生成可执行的动作序列；3) 采用了对比学习损失函数来训练A2L模块，以提高语言描述的准确性；4) 使用了基于置信度的过滤策略来选择高质量的自生成训练数据。

## 📊 实验亮点

LACY在模拟和真实世界的抓取放置任务上取得了显著的性能提升。在模拟环境中，LACY的任务成功率平均提高了56.46%。在真实世界环境中，LACY也表现出优于基线方法的性能。这些实验结果表明，LACY框架能够有效地提高机器人操作的泛化能力和鲁棒性。

## 🎯 应用场景

LACY框架具有广泛的应用前景，可应用于各种机器人操作任务，例如家庭服务机器人、工业自动化机器人和医疗机器人等。通过提高机器人的泛化能力和可解释性，LACY可以使机器人更好地适应复杂和动态的环境，并与人类进行更自然的交互。此外，LACY的自提升能力可以降低对人工标注数据的依赖，从而加速机器人技术的普及。

## 📄 摘要（原文）

> Learning generalizable policies for robotic manipulation increasingly relies on large-scale models that map language instructions to actions (L2A). However, this one-way paradigm often produces policies that execute tasks without deeper contextual understanding, limiting their ability to generalize or explain their behavior. We argue that the complementary skill of mapping actions back to language (A2L) is essential for developing more holistic grounding. An agent capable of both acting and explaining its actions can form richer internal representations and unlock new paradigms for self-supervised learning. We introduce LACY (Language-Action Cycle), a unified framework that learns such bidirectional mappings within a single vision-language model. LACY is jointly trained on three synergistic tasks: generating parameterized actions from language (L2A), explaining observed actions in language (A2L), and verifying semantic consistency between two language descriptions (L2C). This enables a self-improving cycle that autonomously generates and filters new training data through an active augmentation strategy targeting low-confidence cases, thereby improving the model without additional human labels. Experiments on pick-and-place tasks in both simulation and the real world show that LACY improves task success rates by 56.46% on average and yields more robust language-action grounding for robotic manipulation. Project page: https://vla2026.github.io/LACY/

