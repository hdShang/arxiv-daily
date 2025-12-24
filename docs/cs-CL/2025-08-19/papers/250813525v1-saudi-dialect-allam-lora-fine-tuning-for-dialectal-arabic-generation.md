---
layout: default
title: "Saudi-Dialect-ALLaM: LoRA Fine-Tuning for Dialectal Arabic Generation"
---

# Saudi-Dialect-ALLaM: LoRA Fine-Tuning for Dialectal Arabic Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13525" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13525v1</a>
  <a href="https://arxiv.org/pdf/2508.13525.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13525v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13525v1', 'Saudi-Dialect-ALLaM: LoRA Fine-Tuning for Dialectal Arabic Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hassan Barmandah

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-19

**备注**: 7 pages, 6 figures, 2 tables. Code: https://github.com/HasanBGIt/Saudi-Dialect-ALLaM . Dataset and trained weights/adapters are not released. Primary category: cs.CL

---

## 💡 一句话要点

**提出LoRA微调方法以解决阿拉伯方言生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿拉伯语生成` `方言处理` `LoRA微调` `大型语言模型` `自然语言处理` `文本保真度` `方言分类`

## 📋 核心要点

1. 现有的阿拉伯语大型语言模型主要以现代标准阿拉伯语为主，缺乏对沙特方言的有效支持，限制了其在方言生成中的应用。
2. 本文提出了LoRA微调方法，通过使用沙特方言指令数据集，探索了带标签和不带标签的训练方式，以提高方言生成的准确性和多样性。
3. 实验结果表明，Dialect-Token模型在方言控制和文本保真度上均优于多种强大的通用指令模型，显著提升了方言生成的质量。

## 📝 摘要（中文）

阿拉伯语的大型语言模型（LLMs）主要集中在现代标准阿拉伯语（MSA），对沙特方言（如Najdi和Hijazi）的支持有限，影响了其捕捉真实方言变异的能力。本文使用私有的沙特方言指令数据集（包含5466对合成指令-响应对，按50/50分割），对沙特首个基础模型ALLaM-7B-Instruct-preview进行LoRA微调，以实现沙特方言生成。研究了两种变体：一种是在指令前添加显式方言标签的Dialect-Token训练，另一种则省略标签的No-Token训练。评估结果显示，Dialect-Token模型在方言控制上表现最佳，沙特方言生成率从47.97%提升至84.21%，同时MSA泄漏率从32.63%降至6.21%。

## 🔬 方法详解

**问题定义**：本文旨在解决阿拉伯语大型语言模型对沙特方言（Najdi和Hijazi）的生成能力不足的问题。现有模型主要集中在现代标准阿拉伯语，导致方言变异的捕捉能力较弱。

**核心思路**：通过使用私有的沙特方言指令数据集，采用LoRA微调技术，探索在指令中添加方言标签的训练方式，以增强模型对方言的生成能力。

**技术框架**：整体架构包括数据集构建、模型微调和评估三个主要阶段。数据集包含5466对合成指令-响应对，模型微调使用LoRA技术，评估则结合外部方言分类器和文本保真度指标。

**关键创新**：最重要的创新在于Dialect-Token训练方式，通过在指令前添加方言标签，显著提高了方言生成的控制能力和准确性，避免了现有模型常见的元数据标签回声问题。

**关键设计**：在训练过程中，采用了特定的损失函数和网络结构设计，以优化方言生成的质量。实验中对比了不同训练方式的效果，确保了模型在方言生成上的优势。

## 📊 实验亮点

实验结果显示，Dialect-Token模型在方言生成控制上表现优异，沙特方言生成率从47.97%提升至84.21%，MSA泄漏率从32.63%降至6.21%。此外，模型在文本保真度指标chrF++和BERTScore上也有显著提升，分别提高了3.53和0.059，超越了多种强大的通用指令模型。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容生成、客户服务对话系统以及教育领域的方言学习工具。通过提升方言生成的能力，能够更好地满足沙特地区用户的需求，增强人机交互的自然性和流畅性。未来，该技术可能会影响更广泛的阿拉伯语处理任务，促进方言与标准语之间的有效转换。

## 📄 摘要（原文）

> Large language models (LLMs) for Arabic are still dominated by Modern Standard Arabic (MSA), with limited support for Saudi dialects such as Najdi and Hijazi. This underrepresentation hinders their ability to capture authentic dialectal variation. Using a privately curated Saudi Dialect Instruction dataset (Hijazi and Najdi; 5,466 synthetic instruction-response pairs; 50/50 split), we LoRA-tune ALLaM-7B-Instruct-preview, the first foundation model developed in Saudi Arabia, for Saudi dialect generation. We investigate two variants: (i) Dialect-Token training, which prepends an explicit dialect tag to the instruction, and (ii) No-Token training, which omits the tag at formatting time. Evaluation on a held-out test set combines an external dialect classifier with text fidelity metrics (chrF++ and BERTScore) and diversity measures. The Dialect-Token model achieves the best control, raising the Saudi rate from 47.97% to 84.21% and reducing MSA leakage from 32.63% to 6.21%; fidelity also improves (chrF++ +3.53, BERTScore +0.059). Both LoRA variants outperform strong generic instruction models (Falcon-7B-Instruct, Llama-3.1-8B-Instruct, Qwen-2.5-7B-Instruct, AceGPT-v2-8B-Chat, JAIS-13B-Chat) in dialect control and fidelity, while avoiding metadata-tag echoing that these baselines frequently exhibit. We do not release the dataset or any model weights/adapters; instead, we release training/evaluation/inference code and a detailed datasheet (schema and aggregate statistics) to support independent verification.

