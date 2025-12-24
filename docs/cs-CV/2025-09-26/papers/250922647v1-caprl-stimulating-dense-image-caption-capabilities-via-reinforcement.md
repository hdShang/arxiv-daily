---
layout: default
title: "CapRL: Stimulating Dense Image Caption Capabilities via Reinforcement Learning"
---

# CapRL: Stimulating Dense Image Caption Capabilities via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22647" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22647v1</a>
  <a href="https://arxiv.org/pdf/2509.22647.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22647v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22647v1', 'CapRL: Stimulating Dense Image Caption Capabilities via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Long Xing, Xiaoyi Dong, Yuhang Zang, Yuhang Cao, Jianze Liang, Qidong Huang, Jiaqi Wang, Feng Wu, Dahua Lin

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-09-26

**备注**: Code is available at https://github.com/InternLM/CapRL

**🔗 代码/项目**: [GITHUB](https://github.com/InternLM/CapRL)

---

## 💡 一句话要点

**提出CapRL，利用强化学习提升图像描述的稠密性和质量。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图像描述` `强化学习` `视觉-语言模型` `奖励函数` `多模态学习`

## 📋 核心要点

1. 现有图像描述模型依赖监督微调，数据标注成本高昂且模型易于记忆标准答案，泛化能力受限。
2. CapRL利用强化学习，通过奖励函数引导模型生成更有效的描述，使语言模型能据此准确回答图像相关问题。
3. 实验表明，CapRL在多个基准测试中显著提升了图像描述质量，并在Prism评估框架中表现出色。

## 📝 摘要（中文）

图像描述是连接视觉和语言领域的基础任务，在大规模视觉-语言模型（LVLM）的预训练中起着关键作用。目前最先进的图像描述模型通常采用监督微调（SFT）进行训练，这种模式依赖于昂贵且难以扩展的人工标注或专有模型生成的数据。这种方法通常导致模型记忆特定的标准答案，限制了其泛化能力和生成多样化、创造性描述的能力。为了克服SFT的局限性，我们提出将具有可验证奖励的强化学习（RLVR）范式应用于开放式的图像描述任务。然而，一个主要的挑战是为“好的”描述这种本质上主观的概念设计一个客观的奖励函数。我们引入了描述强化学习（CapRL），这是一个新颖的训练框架，它通过效用来重新定义描述质量：高质量的描述应该使非视觉语言模型能够准确地回答关于相应图像的问题。CapRL采用解耦的两阶段流程，其中LVLM生成描述，客观奖励来自独立的、无视觉LLM仅基于该描述回答多项选择题的准确性。作为第一个将RLVR应用于主观图像描述任务的研究，我们证明了CapRL显著增强了多种设置。在由CapRL-3B标注的CapRL-5M描述数据集上进行预训练，在12个基准测试中获得了显著的提升。此外，在Prism框架下进行描述质量评估时，CapRL达到了与Qwen2.5-VL-72B相当的性能，同时超过基线平均8.4%。

## 🔬 方法详解

**问题定义**：现有图像描述模型主要依赖于监督微调（SFT），需要大量人工标注或专有模型生成的数据。这种方式成本高昂且难以扩展，同时模型容易过拟合训练数据，缺乏生成多样化和创造性描述的能力。因此，如何提升图像描述模型的泛化能力和生成质量，同时降低对人工标注的依赖，是本文要解决的核心问题。

**核心思路**：本文的核心思路是将强化学习（RL）应用于图像描述任务，并设计一个基于描述效用的奖励函数。具体来说，高质量的图像描述应该能够使一个独立的语言模型（LLM）准确回答关于图像的问题。通过这种方式，将主观的描述质量转化为客观的可量化的指标，从而利用强化学习来优化图像描述模型的生成策略。

**技术框架**：CapRL采用解耦的两阶段流程。第一阶段，使用一个视觉-语言模型（LVLM）生成图像描述。第二阶段，使用一个独立的、无视觉的语言模型（LLM）基于生成的描述回答关于图像的多项选择题。LLM的回答准确率作为奖励信号，用于训练LVLM的描述生成策略。整个框架包含三个主要模块：图像描述生成器（LVLM）、问题生成器（可选，用于生成更多样的问题）和答案评估器（LLM）。

**关键创新**：CapRL最重要的创新点在于将强化学习与基于效用的奖励函数相结合，用于图像描述任务。与传统的基于人工标注的监督学习方法不同，CapRL通过LLM的回答准确率来衡量描述的质量，从而避免了对大量人工标注的依赖，并鼓励模型生成更有效的描述。此外，CapRL是第一个将具有可验证奖励的强化学习（RLVR）应用于主观图像描述任务的研究。

**关键设计**：CapRL的关键设计包括：1) 使用多项选择题作为评估描述质量的方式，避免了开放式问题答案评估的困难；2) 使用独立的LLM作为答案评估器，避免了LVLM自身评估自身描述的偏差；3) 设计合适的奖励函数，平衡准确率和描述的多样性；4) 使用大规模数据集（CapRL-5M）进行预训练，提升模型的泛化能力。具体参数设置和损失函数细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

CapRL在12个基准测试中获得了显著的提升，表明其在图像描述质量方面具有优越性。在Prism框架下进行描述质量评估时，CapRL达到了与Qwen2.5-VL-72B相当的性能，同时超过基线平均8.4%。这些实验结果表明，CapRL能够有效地提升图像描述模型的性能，并具有很强的竞争力。

## 🎯 应用场景

CapRL具有广泛的应用前景，可用于提升各种视觉-语言模型的图像描述能力，例如智能客服、图像搜索引擎、自动驾驶等。通过生成更准确、更丰富的图像描述，可以提高人机交互的效率和用户体验。此外，CapRL还可以用于生成训练数据，进一步提升视觉-语言模型的性能。

## 📄 摘要（原文）

> Image captioning is a fundamental task that bridges the visual and linguistic domains, playing a critical role in pre-training Large Vision-Language Models (LVLMs). Current state-of-the-art captioning models are typically trained with Supervised Fine-Tuning (SFT), a paradigm that relies on expensive, non-scalable data annotated by humans or proprietary models. This approach often leads to models that memorize specific ground-truth answers, limiting their generality and ability to generate diverse, creative descriptions. To overcome the limitation of SFT, we propose applying the Reinforcement Learning with Verifiable Rewards (RLVR) paradigm to the open-ended task of image captioning. A primary challenge, however, is designing an objective reward function for the inherently subjective nature of what constitutes a "good" caption. We introduce Captioning Reinforcement Learning (CapRL), a novel training framework that redefines caption quality through its utility: a high-quality caption should enable a non-visual language model to accurately answer questions about the corresponding image. CapRL employs a decoupled two-stage pipeline where an LVLM generates a caption, and the objective reward is derived from the accuracy of a separate, vision-free LLM answering Multiple-Choice Questions based solely on that caption. As the first study to apply RLVR to the subjective image captioning task, we demonstrate that CapRL significantly enhances multiple settings. Pretraining on the CapRL-5M caption dataset annotated by CapRL-3B results in substantial gains across 12 benchmarks. Moreover, within the Prism Framework for caption quality evaluation, CapRL achieves performance comparable to Qwen2.5-VL-72B, while exceeding the baseline by an average margin of 8.4%. Code is available here: https://github.com/InternLM/CapRL.

