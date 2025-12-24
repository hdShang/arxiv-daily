---
layout: default
title: "Inverse IFEval: Can LLMs Unlearn Stubborn Training Conventions to Follow Real Instructions?"
---

# Inverse IFEval: Can LLMs Unlearn Stubborn Training Conventions to Follow Real Instructions?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04292" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04292v1</a>
  <a href="https://arxiv.org/pdf/2509.04292.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04292v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04292v1', 'Inverse IFEval: Can LLMs Unlearn Stubborn Training Conventions to Follow Real Instructions?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qinyan Zhang, Xinping Lei, Ruijie Miao, Yu Fu, Haojie Fan, Le Chang, Jiafan Hou, Dingling Zhang, Zhongfei Hou, Ziqiang Yang, Changxin Pu, Fei Hu, Jingkai Liu, Mengyun Liu, Yang Liu, Xiang Gao, Jiaheng Liu, Tong Yang, Zaiyuan Wang, Ge Zhang, Wenhao Huang

**分类**: cs.CL

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出Inverse IFEval基准，评估LLM克服训练偏差并遵循反常指令的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `指令遵循` `认知惯性` `对抗性指令` `评估基准`

## 📋 核心要点

1. 现有LLM在遵循与训练数据相悖的指令时存在困难，表现出认知惯性。
2. 提出Inverse IFEval基准，通过对抗性指令评估LLM克服训练偏差的能力。
3. 实验表明，现有LLM在Inverse IFEval上表现不佳，突出了未来对齐工作的重点。

## 📝 摘要（中文）

大型语言模型(LLMs)在各种任务上表现出色，但常常表现出认知惯性，难以遵循与监督微调(SFT)期间学习到的标准化模式相冲突的指令。为了评估这种局限性，我们提出了Inverse IFEval，这是一个基准，用于衡量模型违反直觉的能力——即覆盖训练引起的偏差并遵守对抗性指令的能力。Inverse IFEval引入了八种此类挑战，包括问题纠正、故意文本缺陷、无注释代码和反事实回答。通过人机协作流程，我们构建了一个包含23个领域中1012个高质量中英文问题的数据集，并在优化的LLM-as-a-Judge框架下进行了评估。对现有领先LLM的实验证明了我们提出的Inverse IFEval基准的必要性。我们的研究结果强调，未来的对齐工作不仅应追求流畅性和事实正确性，还应考虑在非常规环境下的适应性。我们希望Inverse IFEval既可以作为诊断工具，又可以作为开发方法的基石，以减轻认知惯性，减少对狭隘模式的过度拟合，并最终提高LLM在各种不可预测的现实场景中的指令遵循可靠性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在面对与训练数据分布不同的、具有对抗性的指令时，难以有效遵循的问题。现有方法主要关注LLM的流畅性和事实正确性，而忽略了其在非常规情境下的适应能力，导致模型容易受到训练偏差的影响，无法灵活应对真实世界中复杂多变的指令。

**核心思路**：论文的核心思路是构建一个专门的评估基准，即Inverse IFEval，用于衡量LLM克服训练偏差并遵循反常指令的能力。通过设计一系列具有挑战性的对抗性指令，例如问题纠正、故意文本缺陷等，来迫使LLM打破其在监督微调(SFT)期间学习到的标准化模式，从而评估其认知灵活性和指令遵循的可靠性。

**技术框架**：Inverse IFEval的构建流程主要包括以下几个阶段：
1. **挑战类型定义**：定义八种类型的对抗性指令挑战，涵盖问题纠正、文本缺陷、无注释代码、反事实回答等。
2. **数据集构建**：通过人机协作的方式，针对每种挑战类型，构建高质量的中英文问题数据集，覆盖23个领域。
3. **评估框架**：采用优化的LLM-as-a-Judge框架，利用LLM作为裁判，评估模型在Inverse IFEval上的表现。
4. **实验分析**：对现有领先的LLM进行实验，分析其在不同挑战类型上的表现，并提出改进建议。

**关键创新**：该论文最重要的技术创新点在于提出了Inverse IFEval这一全新的评估基准，它不同于以往关注流畅性和事实正确性的评估方法，而是专注于评估LLM在对抗性指令下的适应能力和认知灵活性。这种评估方式能够更全面地反映LLM在真实世界复杂场景中的表现，并为未来的模型对齐工作提供新的方向。

**关键设计**：Inverse IFEval的关键设计包括：
1. **对抗性指令类型**：精心设计的八种对抗性指令类型，能够有效挑战LLM的认知惯性。
2. **人机协作的数据集构建**：保证数据集的高质量和多样性。
3. **优化的LLM-as-a-Judge框架**：确保评估的客观性和可靠性。

## 📊 实验亮点

实验结果表明，现有领先的LLM在Inverse IFEval基准上表现不佳，尤其是在问题纠正、文本缺陷和反事实回答等挑战类型上。这表明，即使是经过大规模训练的LLM，仍然存在严重的认知惯性问题，难以有效遵循对抗性指令。该研究强调了未来对齐工作不仅要关注流畅性和事实正确性，更要关注LLM在非常规环境下的适应能力。

## 🎯 应用场景

该研究成果可应用于提升LLM在各种实际场景中的可靠性和适应性，例如在自动驾驶、智能客服、医疗诊断等领域，LLM需要能够理解并执行不符合常规的指令。通过使用Inverse IFEval作为诊断工具，可以帮助开发者识别LLM的潜在缺陷，并开发相应的改进方法，从而提高LLM在复杂和不可预测环境中的表现。

## 📄 摘要（原文）

> Large Language Models (LLMs) achieve strong performance on diverse tasks but often exhibit cognitive inertia, struggling to follow instructions that conflict with the standardized patterns learned during supervised fine-tuning (SFT). To evaluate this limitation, we propose Inverse IFEval, a benchmark that measures models Counter-intuitive Abilitytheir capacity to override training-induced biases and comply with adversarial instructions. Inverse IFEval introduces eight types of such challenges, including Question Correction, Intentional Textual Flaws, Code without Comments, and Counterfactual Answering. Using a human-in-the-loop pipeline, we construct a dataset of 1012 high-quality Chinese and English questions across 23 domains, evaluated under an optimized LLM-as-a-Judge framework. Experiments on existing leading LLMs demonstrate the necessity of our proposed Inverse IFEval benchmark. Our findings emphasize that future alignment efforts should not only pursue fluency and factual correctness but also account for adaptability under unconventional contexts. We hope that Inverse IFEval serves as both a diagnostic tool and a foundation for developing methods that mitigate cognitive inertia, reduce overfitting to narrow patterns, and ultimately enhance the instruction-following reliability of LLMs in diverse and unpredictable real-world scenarios.

