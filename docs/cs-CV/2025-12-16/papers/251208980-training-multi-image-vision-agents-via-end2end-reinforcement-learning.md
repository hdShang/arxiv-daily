---
layout: default
title: Training Multi-Image Vision Agents via End2End Reinforcement Learning
---

# Training Multi-Image Vision Agents via End2End Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.08980" class="toolbar-btn" target="_blank">📄 arXiv: 2512.08980</a>
  <a href="https://arxiv.org/pdf/2512.08980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.08980" onclick="toggleFavorite(this, '2512.08980', 'Training Multi-Image Vision Agents via End2End Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengqi Dong, Chuhuai Yue, Hang He, Rongge Mao, Fenghe Tang, S Kevin Zhou, Zekun Xu, Xiaohan Wang, Jiajun Chai, Wei Lin, Guojun Yin

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出IMAgent，通过端到端强化学习训练多图视觉Agent，解决复杂多图QA任务。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多图视觉Agent` `强化学习` `视觉语言模型` `工具使用` `多模态学习`

## 📋 核心要点

1. 现有基于VLM的Agent在多图QA任务中表现不足，因为它们通常仅限于单图输入，无法充分利用工具。
2. IMAgent通过端到端强化学习训练，并引入视觉反思和确认工具，使Agent能够更好地处理多图信息并进行推理。
3. 实验表明，IMAgent在多图QA数据集上取得了显著的性能提升，同时在单图基准上保持了竞争力。

## 📝 摘要（中文）

本文提出IMAgent，一个开源的视觉Agent，通过端到端强化学习训练，专门用于处理复杂的多图任务。该方法利用多Agent系统生成具有挑战性和视觉丰富性的多图QA对，以充分激活基础VLM的工具使用潜力。通过人工验证，构建了包含1万个样本的MIFG-QA数据集，用于训练和评估。针对VLM在推理过程中可能忽略视觉输入的问题，开发了视觉反思和确认工具，使模型能够在推理过程中主动重新分配对图像内容的注意力。受益于精心设计的动作轨迹两级掩码策略，IMAgent通过纯强化学习训练实现了稳定的工具使用行为，无需昂贵的监督微调数据。大量实验表明，IMAgent在现有单图基准上保持了强大的性能，并在提出的多图数据集上取得了显著的改进，分析结果为研究社区提供了可操作的见解。

## 🔬 方法详解

**问题定义**：现有基于视觉语言模型（VLM）的Agent，如OpenAI O3，虽然可以通过工具使用进行“图像思考”，但大多数开源方法仅限于单张图像输入。这使得它们在处理需要多张图像信息的真实世界QA任务时表现不佳。因此，需要一种能够有效处理多图输入，并充分利用VLM工具使用能力的方法。

**核心思路**：IMAgent的核心思路是利用端到端强化学习，训练一个能够处理多图输入的视觉Agent。通过构建一个多Agent系统，生成具有挑战性的多图QA对，并设计视觉反思和确认工具，使Agent能够更好地理解和利用图像信息。此外，还采用了动作轨迹两级掩码策略，以稳定工具的使用行为。

**技术框架**：IMAgent的技术框架主要包括以下几个部分：1) 多Agent系统：用于生成具有挑战性的多图QA对，以训练Agent的工具使用能力。2) 视觉反思和确认工具：用于帮助Agent在推理过程中重新关注图像内容，避免忽略视觉输入。3) 强化学习训练：使用端到端强化学习训练Agent，使其能够学习如何有效地使用工具和处理多图信息。4) 动作轨迹两级掩码策略：用于稳定Agent的工具使用行为，避免出现不稳定的情况。

**关键创新**：IMAgent的关键创新在于以下几个方面：1) 提出了一个基于端到端强化学习的多图视觉Agent训练方法。2) 设计了视觉反思和确认工具，以解决VLM在推理过程中可能忽略视觉输入的问题。3) 提出了动作轨迹两级掩码策略，以稳定Agent的工具使用行为。4) 构建了一个包含1万个样本的多图QA数据集MIFG-QA，用于训练和评估Agent的性能。

**关键设计**：IMAgent的关键设计包括：1) 多Agent系统的设计，需要考虑如何生成具有挑战性的多图QA对。2) 视觉反思和确认工具的设计，需要考虑如何有效地帮助Agent重新关注图像内容。3) 强化学习训练的奖励函数设计，需要考虑如何引导Agent学习有效使用工具和处理多图信息。4) 动作轨迹两级掩码策略的设计，需要考虑如何稳定Agent的工具使用行为。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.08980/figure/attention_decay4.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.08980/figure/model.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.08980/figure/data_construct.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

IMAgent在提出的多图数据集MIFG-QA上取得了显著的性能提升，相较于基线方法，性能提升了XX%。同时，IMAgent在现有的单图基准上保持了强大的性能，表明其具有良好的泛化能力。实验结果表明，视觉反思和确认工具以及动作轨迹两级掩码策略对IMAgent的性能提升起到了关键作用。

## 🎯 应用场景

IMAgent具有广泛的应用前景，例如智能客服、自动驾驶、医学图像分析等领域。它可以帮助Agent更好地理解和利用多图信息，从而提高其在复杂任务中的性能。例如，在智能客服领域，IMAgent可以用于处理用户上传的多张图片，从而更准确地理解用户的问题并提供相应的解决方案。在自动驾驶领域，IMAgent可以用于处理多个摄像头拍摄的图像，从而更准确地感知周围环境并做出相应的决策。

## 📄 摘要（原文）

> Recent VLM-based agents aim to replicate OpenAI O3's ``thinking with images" via tool use, but most open-source methods limit input to a single image, falling short on real-world multi-image QA tasks. To address this, we propose IMAgent, an open-source vision agent trained via end-to-end reinforcement learning dedicated for complex multi-image tasks. By leveraging a multi-agent system, we generate challenging and visually-rich multi-image QA pairs to fully activate the tool-use potential of the base VLM. Through manual verification, we obtain MIFG-QA, comprising 10k samples for training and evaluation. With deeper reasoning steps, VLMs may increasingly ignore visual inputs. We therefore develop two specialized tools for visual reflection and confirmation, allowing the model to proactively reallocate its attention to image content during inference. Benefiting from our well-designed action-trajectory two-level mask strategy, IMAgent achieves stable tool use behavior via pure RL training without requiring costly supervised fine-tuning data. Extensive experiments demonstrate that IMAgent maintains strong performance on existing single-image benchmarks while achieving substantial improvements on our proposed multi-image dataset, with our analysis providing actionable insights for the research community. Codes and data will be released soon.

