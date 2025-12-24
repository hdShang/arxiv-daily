---
layout: default
title: "Self-Consistency as a Free Lunch: Reducing Hallucinations in Vision-Language Models via Self-Reflection"
---

# Self-Consistency as a Free Lunch: Reducing Hallucinations in Vision-Language Models via Self-Reflection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23236" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23236v1</a>
  <a href="https://arxiv.org/pdf/2509.23236.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23236v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23236v1', 'Self-Consistency as a Free Lunch: Reducing Hallucinations in Vision-Language Models via Self-Reflection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingfei Han, Haihong Hao, Jinxing Zhou, Zhihui Li, Yuhui Zheng, Xueqing Deng, Linjie Yang, Xiaojun Chang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出基于自反思的自洽性方法，减少视觉-语言模型中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `幻觉减少` `自洽性` `自监督学习` `自反思` `事实基础` `指令遵循`

## 📋 核心要点

1. 现有视觉-语言模型易产生幻觉，影响可靠性，且依赖大量人工标注或外部模型监督。
2. 论文提出利用模型自身在长回复和短答案间的自洽性，自动生成高质量训练数据，无需额外标注。
3. 实验表明，该方法在多个基准测试中显著提升了事实基础和可靠性，并保持了指令遵循能力。

## 📝 摘要（中文）

视觉-语言模型经常产生幻觉，生成不存在的对象或不准确的属性，从而降低输出的可靠性。现有方法通常依赖大量人工标注或来自更强大模型的外部监督来解决这些问题。本文提出了一种新颖的框架，利用模型在长回复和短答案之间的自洽性来生成训练所需的偏好对。我们观察到，简短的二元问题往往产生高度可靠的回复，可用于查询目标模型以评估和排序其生成的回复。具体来说，我们设计了一个自反思流程，将详细的模型回复与简洁的二元答案进行比较，并利用不一致信号自动生成高质量的训练数据，无需人工标注或基于外部模型的监督。通过仅依赖自洽性而非外部监督，我们的方法提供了一种可扩展且高效的解决方案，可有效减少使用未标记数据的幻觉。在多个基准测试（即AMBER、MultiObject-Hal (ROPE)、Object HalBench和MMHal-Bench）上的大量实验表明，在事实基础和可靠性方面有显著改进。此外，我们的方法保持了强大的指令遵循能力，LLaVA-Bench和MMBench上的性能提升证明了这一点。

## 🔬 方法详解

**问题定义**：视觉-语言模型在生成描述时，容易出现“幻觉”现象，即生成与图像内容不符的对象或属性。现有方法主要依赖于人工标注的数据或更强大的外部模型进行监督训练，成本高昂且难以扩展。因此，如何利用无标注数据，有效减少视觉-语言模型中的幻觉问题是一个重要的挑战。

**核心思路**：论文的核心思路是利用模型自身的自洽性作为监督信号。具体来说，模型对于同一个图像的详细描述（长回复）和简短的是非判断（短答案）应该保持一致。如果模型生成的长回复与通过短答案验证的结果不一致，则认为该长回复存在幻觉。通过这种自反思机制，可以自动生成用于训练的偏好对，引导模型学习更可靠的输出。

**技术框架**：该方法主要包含一个自反思流程。首先，模型生成对图像的详细描述（长回复）。然后，针对该描述生成一系列简短的二元问题，并让模型回答这些问题（短答案）。接着，比较长回复和短答案之间的一致性。如果存在不一致，则将该长回复标记为存在幻觉。最后，利用这些标记的数据生成偏好对，用于训练模型，使其更倾向于生成与短答案一致的长回复。

**关键创新**：该方法最重要的创新在于利用了模型自身的自洽性作为监督信号，无需人工标注或外部模型。这种自监督的方式降低了训练成本，提高了可扩展性。此外，通过比较长回复和短答案的一致性，可以有效地检测和纠正模型中的幻觉问题。

**关键设计**：关键设计包括：1) 如何生成有效的二元问题，以覆盖长回复中的关键信息；2) 如何定义长回复和短答案之间的一致性标准；3) 如何利用不一致信号生成高质量的偏好对，以指导模型的训练。具体参数设置和损失函数细节在论文中未明确给出，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在AMBER、MultiObject-Hal (ROPE)、Object HalBench和MMHal-Bench等多个基准测试中显著提高了事实基础和可靠性。同时，该方法在LLaVA-Bench和MMBench上保持了强大的指令遵循能力，表明其在减少幻觉的同时，没有牺牲模型的通用性能。具体的性能提升数据在论文中给出，此处省略。

## 🎯 应用场景

该研究成果可广泛应用于需要高度可靠的视觉-语言任务中，例如自动驾驶、医疗影像诊断、智能客服等。通过减少模型中的幻觉，可以提高系统的安全性和可信度，从而促进视觉-语言模型在实际场景中的应用。此外，该方法无需人工标注的特性，使其具有很高的应用潜力。

## 📄 摘要（原文）

> Vision-language models often hallucinate details, generating non-existent objects or inaccurate attributes that compromise output reliability. Existing methods typically address these issues via extensive human annotations or external supervision from more powerful models. In this work, we present a novel framework that leverages the model's self-consistency between long responses and short answers to generate preference pairs for training. We observe that short binary questions tend to yield highly reliable responses, which can be used to query the target model to evaluate and rank its generated responses. Specifically, we design a self-reflection pipeline where detailed model responses are compared against concise binary answers, and inconsistency signals are utilized to automatically curate high-quality training data without human annotations or external model-based supervision. By relying solely on self-consistency rather than external supervision, our method offers a scalable and efficient solution that effectively reduces hallucinations using unlabeled data. Extensive experiments on multiple benchmarks, i.e., AMBER, MultiObject-Hal (ROPE), Object HalBench, and MMHal-Bench, demonstrate significant improvements in factual grounding and reliability. Moreover, our approach maintains robust instruction-following ability, as evidenced by enhanced performance on LLaVA-Bench and MMBench.

