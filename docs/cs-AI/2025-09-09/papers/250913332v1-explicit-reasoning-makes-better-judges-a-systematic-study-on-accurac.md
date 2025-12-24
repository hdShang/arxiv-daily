---
layout: default
title: "Explicit Reasoning Makes Better Judges: A Systematic Study on Accuracy, Efficiency, and Robustness"
---

# Explicit Reasoning Makes Better Judges: A Systematic Study on Accuracy, Efficiency, and Robustness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13332" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13332v1</a>
  <a href="https://arxiv.org/pdf/2509.13332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13332v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13332v1', 'Explicit Reasoning Makes Better Judges: A Systematic Study on Accuracy, Efficiency, and Robustness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pratik Jayarao, Himanshu Gupta, Neeraj Varshney, Chaitanya Dwivedi

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**研究表明，在LLM评判任务中，显式推理模型在准确性、效率和鲁棒性上更优。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `显式推理` `自动评判` `鲁棒性` `偏差分析` `RewardBench` `Qwen 3`

## 📋 核心要点

1. 现有LLM评判方法缺乏效率和鲁棒性，难以保证在各种偏差条件下的评判一致性。
2. 论文提出采用显式推理的LLM作为评判器，旨在提升评判的准确性、效率和鲁棒性。
3. 实验结果表明，显式推理模型在准确性上提升显著，且在多种偏差条件下表现出更强的鲁棒性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）越来越多地被用作基准测试和奖励建模中的自动评判器，确保其可靠性、效率和鲁棒性至关重要。本文对“思考型”和“非思考型”LLM在LLM-as-a-judge范式中进行了系统比较，使用了相对较小规模的开源Qwen 3模型（0.6B、1.7B和4B参数）。我们评估了RewardBench任务上的准确性和计算效率（FLOPs），并进一步研究了非思考型模型的增强策略，包括上下文学习、规则引导评判、基于参考的评估和n-best聚合。结果表明，尽管进行了这些增强，非思考型模型通常不如思考型模型。思考型模型在准确性上提高了约10个百分点，计算开销很小（低于2倍），而像少样本学习这样的增强策略以更高的成本（>8倍）提供了适度的收益。偏差和鲁棒性分析进一步表明，思考型模型在各种偏差条件下（如位置偏差、从众偏差、身份偏差、多样性偏差和随机偏差）保持了显著更高的一致性（平均高6%）。我们还将实验扩展到多语言环境，结果证实显式推理的优势超越了英语。总的来说，我们的工作得出了一些重要的发现，这些发现提供了系统的证据，表明显式推理在LLM-as-a-judge范式中不仅在准确性和效率方面，而且在鲁棒性方面都提供了明显的优势。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型作为自动评判器时，在准确性、效率和鲁棒性方面存在的不足。现有方法，特别是“非思考型”模型，在面对各种偏差时，评判结果的一致性较差，且计算成本较高。

**核心思路**：论文的核心思路是利用“思考型”LLM，即具有显式推理能力的LLM，来提升评判的质量。通过让模型在给出最终判断之前进行显式的推理过程，可以减少偏差的影响，提高评判的准确性和鲁棒性。

**技术框架**：论文采用LLM-as-a-judge范式，使用开源的Qwen 3模型作为评判器。主要分为两个类型的模型：思考型和非思考型。对非思考型模型，论文还探索了多种增强策略，包括上下文学习、规则引导评判、基于参考的评估和n-best聚合。实验在RewardBench任务上进行，评估指标包括准确性和计算效率（FLOPs）。

**关键创新**：论文的关键创新在于系统性地比较了“思考型”和“非思考型”LLM在评判任务中的表现，并证明了显式推理在准确性、效率和鲁棒性方面的优势。此外，论文还深入研究了各种偏差对评判结果的影响，并验证了显式推理模型在应对这些偏差时的优越性。

**关键设计**：论文使用了不同规模的Qwen 3模型（0.6B、1.7B和4B参数）进行实验。对于思考型模型，关键在于设计合适的prompt，引导模型进行显式推理。对于非思考型模型，论文尝试了多种增强策略，例如，上下文学习通过提供少量的示例来引导模型进行评判；规则引导评判则通过提供明确的评判标准来减少偏差。

## 📊 实验亮点

实验结果表明，思考型模型在准确性上比非思考型模型高出约10个百分点，且计算开销增加较小（低于2倍）。相比之下，即使采用少样本学习等增强策略，非思考型模型在准确性上的提升也相对有限，且计算成本更高（>8倍）。此外，思考型模型在各种偏差条件下表现出更强的鲁棒性，平均一致性高出6%。多语言实验也验证了显式推理的优势。

## 🎯 应用场景

该研究成果可应用于自动化评估系统、奖励模型构建、以及其他需要高质量、高可靠性评判的场景。例如，可以用于自动评估学生的作业、评估机器翻译的质量、或者在强化学习中作为奖励函数，提升智能体的学习效率和效果。未来的研究可以进一步探索如何优化显式推理过程，以及如何将该方法应用于更复杂的评判任务。

## 📄 摘要（原文）

> As Large Language Models (LLMs) are increasingly adopted as automated judges in benchmarking and reward modeling, ensuring their reliability, efficiency, and robustness has become critical. In this work, we present a systematic comparison of "thinking" and "non-thinking" LLMs in the LLM-as-a-judge paradigm using open-source Qwen 3 models of relatively small sizes (0.6B, 1.7B, and 4B parameters). We evaluate both accuracy and computational efficiency (FLOPs) on RewardBench tasks, and further examine augmentation strategies for non-thinking models, including in-context learning, rubric-guided judging, reference-based evaluation, and n-best aggregation. Our results show that despite these enhancements, non-thinking models generally fall short of their thinking counterparts. Our results show that thinking models achieve approximately 10% points higher accuracy with little overhead (under 2x), in contrast to augmentation strategies like few-shot learning, which deliver modest gains at a higher cost (>8x). Bias and robustness analyses further demonstrate that thinking models maintain significantly greater consistency under a variety of bias conditions such as positional, bandwagon, identity, diversity, and random biases (6% higher on average). We further extend our experiments to the multilingual setting and our results confirm that explicit reasoning extends its benefits beyond English. Overall, our work results in several important findings that provide systematic evidence that explicit reasoning offers clear advantages in the LLM-as-a-judge paradigm not only in accuracy and efficiency but also in robustness.

