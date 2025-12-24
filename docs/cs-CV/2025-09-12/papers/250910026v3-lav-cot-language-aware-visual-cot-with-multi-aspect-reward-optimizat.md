---
layout: default
title: "LaV-CoT: Language-Aware Visual CoT with Multi-Aspect Reward Optimization for Real-World Multilingual VQA"
---

# LaV-CoT: Language-Aware Visual CoT with Multi-Aspect Reward Optimization for Real-World Multilingual VQA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10026" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10026v3</a>
  <a href="https://arxiv.org/pdf/2509.10026.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10026v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10026v3', 'LaV-CoT: Language-Aware Visual CoT with Multi-Aspect Reward Optimization for Real-World Multilingual VQA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Huang, Zhiya Tan, Shutao Gong, Fanwei Zeng, Joey Tianyi Zhou, Changtao Miao, Huazhe Tan, Weibin Yao, Jianshu Li

**分类**: cs.CV

**发布日期**: 2025-09-12 (更新: 2025-10-10)

**备注**: 12 Pages, 12 Figures, 3 Tables

**🔗 代码/项目**: [GITHUB](https://github.com/HJNVR/LaV-CoT)

---

## 💡 一句话要点

**提出LaV-CoT框架，通过多方面奖励优化，解决真实世界多语言VQA问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言视觉问答` `思维链` `多模态推理` `奖励优化` `语言感知` `数据生成` `策略优化`

## 📋 核心要点

1. 现有mVQA方法主要依赖文本CoT，缺乏对多语言多模态推理的有效支持，限制了实际应用。
2. LaV-CoT提出语言感知的视觉CoT框架，包含多阶段推理流程和多方面奖励优化，提升性能。
3. 实验表明，LaV-CoT在多个数据集上显著优于现有模型，并在真实世界数据上验证了有效性。

## 📝 摘要（中文）

随着大型视觉语言模型（VLMs）的发展，它们在多语言视觉问答（mVQA）方面的能力得到了显著提高。思维链（CoT）推理已被证明可以增强可解释性和复杂推理。然而，大多数现有方法主要依赖于文本CoT，并且对多语言多模态推理的支持有限，从而限制了它们在实际应用中的部署。为了解决这一差距，我们引入了LaV-CoT，这是第一个具有多方面奖励优化的语言感知视觉CoT框架。LaV-CoT包含一个可解释的多阶段推理流程，包括带有边界框的文本摘要、语言识别、空间对象级描述和逐步逻辑推理。遵循此推理流程，我们设计了一种自动数据管理方法，该方法通过迭代生成、校正和细化来生成多语言CoT注释，从而实现可扩展的高质量训练数据。为了提高推理和泛化能力，LaV-CoT采用了一种两阶段训练范例，将监督微调（SFT）与语言感知组相对策略优化（GRPO）相结合，并以可验证的多方面奖励（包括语言一致性、结构准确性和语义对齐）为指导。在包括MMMB、Multilingual MMBench和MTVQA在内的公共数据集上的大量评估表明，LaV-CoT的准确率比类似规模的开源基线提高了高达~9.5%，甚至超过了规模大2倍的模型约~2.6%。此外，LaV-CoT的性能优于GPT-4o-0513和Gemini-2.5-flash等先进的专有模型。我们进一步进行了在线A/B测试，以验证我们的方法在真实世界数据上的有效性，突出了其在工业部署中的有效性。我们的代码可在以下链接获得：https://github.com/HJNVR/LaV-CoT

## 🔬 方法详解

**问题定义**：论文旨在解决真实世界多语言视觉问答（mVQA）问题。现有方法主要依赖于文本思维链（CoT），缺乏对多语言和多模态信息的有效利用，导致推理能力不足，难以适应复杂场景。此外，缺乏高质量的多语言CoT数据也是一个挑战。

**核心思路**：LaV-CoT的核心思路是构建一个语言感知的视觉CoT框架，通过多阶段推理流程和多方面奖励优化，增强模型的多语言多模态推理能力。该方法显式地考虑了语言信息，并利用视觉信息辅助推理，从而提高模型的准确性和泛化能力。

**技术框架**：LaV-CoT包含以下主要模块：1) **文本摘要与边界框（BBox）**：提取图像相关文本信息和目标位置。2) **语言识别**：确定输入问题的语言。3) **空间对象级描述**：生成图像中对象的详细描述。4) **逐步逻辑推理**：基于以上信息进行逐步推理，最终得出答案。此外，论文还设计了自动数据生成方法，迭代生成、校正和细化多语言CoT数据。训练过程分为两个阶段：监督微调（SFT）和语言感知组相对策略优化（GRPO）。

**关键创新**：LaV-CoT的关键创新在于：1) 提出了语言感知的视觉CoT框架，显式地考虑了语言信息。2) 设计了多阶段推理流程，将复杂推理过程分解为多个可解释的步骤。3) 提出了多方面奖励优化方法，利用语言一致性、结构准确性和语义对齐等指标指导模型训练。4) 提出了自动数据生成方法，解决了多语言CoT数据稀缺的问题。

**关键设计**：在训练阶段，使用了语言感知组相对策略优化（GRPO），该方法根据语言类型对样本进行分组，并使用相对策略优化算法进行训练，从而提高模型的泛化能力。多方面奖励函数综合考虑了语言一致性、结构准确性和语义对齐等因素，从而更好地指导模型学习。自动数据生成方法通过迭代生成、校正和细化，保证了数据的质量和多样性。

## 📊 实验亮点

LaV-CoT在MMMB、Multilingual MMBench和MTVQA等数据集上取得了显著的性能提升，相比同等规模的开源模型，准确率提升高达9.5%，甚至超越了规模是其两倍的模型2.6%。此外，LaV-CoT的性能优于GPT-4o-0513和Gemini-2.5-flash等先进的专有模型。在线A/B测试也验证了该方法在真实世界数据上的有效性。

## 🎯 应用场景

LaV-CoT框架可应用于智能客服、教育辅助、跨境电商等领域。例如，在智能客服中，可以帮助用户理解多语言的商品信息和使用说明；在教育辅助中，可以帮助学生理解多语言的教材和学习资料。该研究有助于提升多语言环境下人机交互的智能化水平，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> As large vision language models (VLMs) advance, their capabilities in multilingual visual question answering (mVQA) have significantly improved. Chain-of-thought (CoT) reasoning has been proven to enhance interpretability and complex reasoning. However, most existing approaches rely primarily on textual CoT and provide limited support for multilingual multimodal reasoning, constraining their deployment in real-world applications. To address this gap, we introduce LaV-CoT, the first Language-aware Visual CoT framework with Multi-Aspect Reward Optimization. LaV-CoT incorporates an interpretable multi-stage reasoning pipeline consisting of Text Summary with Bounding Box (BBox), Language Identification, Spatial Object-level Captioning, and Step-by-step Logical Reasoning. Following this reasoning pipeline, we design an automated data curation method that generates multilingual CoT annotations through iterative generation, correction, and refinement, enabling scalable and high-quality training data. To improve reasoning and generalization, LaV-CoT adopts a two-stage training paradigm combining Supervised Fine-Tuning (SFT) with Language-aware Group Relative Policy Optimization (GRPO), guided by verifiable multi-aspect rewards including language consistency, structural accuracy, and semantic alignment. Extensive evaluations on public datasets including MMMB, Multilingual MMBench, and MTVQA show that LaV-CoT achieves up to ~9.5% accuracy improvements over open-source baselines of similar size and even surpasses models with 2$\times$ larger scales by ~2.6%. Moreover, LaV-CoT outperforms advanced proprietary models such as GPT-4o-0513 and Gemini-2.5-flash. We further conducted an online A/B test to validate our method on real-world data, highlighting its effectiveness for industrial deployment. Our code is available at this link: https://github.com/HJNVR/LaV-CoT

