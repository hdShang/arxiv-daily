---
layout: default
title: Training Multi-Image Vision Agents via End2End Reinforcement Learning
---

# Training Multi-Image Vision Agents via End2End Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.08980" class="toolbar-btn" target="_blank">📄 arXiv: 2512.08980v2</a>
  <a href="https://arxiv.org/pdf/2512.08980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.08980v2" onclick="toggleFavorite(this, '2512.08980v2', 'Training Multi-Image Vision Agents via End2End Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengqi Dong, Chuhuai Yue, Hang He, Rongge Mao, Fenghe Tang, S Kevin Zhou, Zekun Xu, Xiaohan Wang, Jiajun Chai, Wei Lin, Guojun Yin

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-05 (更新: 2025-12-16)

---

## 💡 一句话要点

**提出IMAgent，通过端到端强化学习训练多图视觉Agent，解决复杂多图QA任务。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多图QA` `视觉Agent` `强化学习` `工具使用` `视觉语言模型`

## 📋 核心要点

1. 现有基于VLM的Agent在工具使用方面存在局限，大多仅限于单张图像输入，难以应对真实世界的多图QA任务。
2. IMAgent通过端到端强化学习训练，并引入多Agent系统生成具有挑战性的多图QA对，从而提升VLM的工具使用能力。
3. 实验表明，IMAgent在多图QA任务上取得了显著提升，同时在单图基准测试中保持了竞争力。

## 📝 摘要（中文）

本文提出IMAgent，一个开源的视觉Agent，通过端到端强化学习训练，专门用于处理复杂的多图任务。利用多Agent系统，生成具有挑战性和视觉丰富性的多图QA对，充分激活基础VLM的工具使用潜力。通过人工验证，构建了包含1万个样本的MIFG-QA数据集，用于训练和评估。针对VLM在推理过程中可能忽略视觉输入的问题，开发了视觉反思和确认工具，使模型能够在推理过程中主动重新分配对图像内容的注意力。受益于精心设计的动作轨迹两级掩码策略，IMAgent通过纯强化学习训练实现了稳定的工具使用行为，无需昂贵的监督微调数据。大量实验表明，IMAgent在现有单图基准上保持了强大的性能，并在提出的多图数据集上取得了显著的改进，分析为研究社区提供了可操作的见解。代码和数据即将发布。

## 🔬 方法详解

**问题定义**：现有基于视觉语言模型（VLM）的Agent在处理多图QA任务时存在不足，主要原因是它们通常只接受单张图像作为输入，这限制了它们在需要综合多张图像信息才能完成的任务中的应用。现有的开源方法难以有效利用VLM的工具使用能力来解决复杂的多图推理问题。

**核心思路**：本文的核心思路是通过端到端强化学习来训练一个能够有效利用多张图像信息的视觉Agent。通过设计一个多Agent系统来生成具有挑战性的多图QA对，从而训练VLM的工具使用能力。此外，为了解决VLM在推理过程中可能忽略视觉输入的问题，引入了视觉反思和确认工具，促使模型更加关注图像内容。

**技术框架**：IMAgent的整体框架包含以下几个主要模块：1) 多Agent数据生成器：负责生成具有挑战性的多图QA对，用于训练Agent。2) 基于VLM的Agent：作为核心推理模块，负责接收图像和问题，并输出答案。3) 视觉反思和确认工具：用于在推理过程中重新分配对图像内容的注意力。4) 强化学习训练模块：使用精心设计的奖励函数和动作轨迹掩码策略，训练Agent的工具使用能力。

**关键创新**：本文的关键创新在于以下几个方面：1) 提出了一个基于多Agent系统的多图QA数据生成方法，能够生成具有挑战性的训练数据。2) 设计了视觉反思和确认工具，解决了VLM在推理过程中可能忽略视觉输入的问题。3) 提出了一个动作轨迹两级掩码策略，使得Agent能够通过纯强化学习训练实现稳定的工具使用行为，无需依赖昂贵的监督微调数据。

**关键设计**：在数据生成方面，设计了不同的Agent角色，分别负责生成问题、选择图像和提供答案，从而保证数据的多样性和挑战性。在强化学习训练方面，使用了稀疏奖励函数，鼓励Agent采取正确的动作序列。动作轨迹两级掩码策略通过限制Agent在不同阶段可以采取的动作，从而提高训练的稳定性和效率。具体参数设置和网络结构细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

IMAgent在提出的多图数据集MIFG-QA上取得了显著的性能提升，超越了现有的单图Agent。同时，IMAgent在现有的单图基准测试中保持了竞争力，表明其具有良好的泛化能力。通过消融实验，验证了视觉反思和确认工具以及动作轨迹掩码策略的有效性。具体的性能数据和提升幅度在论文中进行了详细展示（未知）。

## 🎯 应用场景

IMAgent具有广泛的应用前景，例如智能客服、医学图像诊断、遥感图像分析等领域。它可以帮助用户从多张图像中提取关键信息，并进行深入的推理和决策。未来，IMAgent可以进一步扩展到其他多模态任务中，例如视频理解、机器人导航等，为人工智能应用带来更强大的能力。

## 📄 摘要（原文）

> Recent VLM-based agents aim to replicate OpenAI O3's ``thinking with images" via tool use, but most open-source methods limit input to a single image, falling short on real-world multi-image QA tasks. To address this, we propose IMAgent, an open-source vision agent trained via end-to-end reinforcement learning dedicated for complex multi-image tasks. By leveraging a multi-agent system, we generate challenging and visually-rich multi-image QA pairs to fully activate the tool-use potential of the base VLM. Through manual verification, we obtain MIFG-QA, comprising 10k samples for training and evaluation. With deeper reasoning steps, VLMs may increasingly ignore visual inputs. We therefore develop two specialized tools for visual reflection and confirmation, allowing the model to proactively reallocate its attention to image content during inference. Benefiting from our well-designed action-trajectory two-level mask strategy, IMAgent achieves stable tool use behavior via pure RL training without requiring costly supervised fine-tuning data. Extensive experiments demonstrate that IMAgent maintains strong performance on existing single-image benchmarks while achieving substantial improvements on our proposed multi-image dataset, with our analysis providing actionable insights for the research community. Codes and data will be released soon.

