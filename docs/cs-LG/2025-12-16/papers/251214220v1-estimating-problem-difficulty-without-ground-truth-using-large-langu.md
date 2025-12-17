---
layout: default
title: Estimating problem difficulty without ground truth using Large Language Model comparisons
---

# Estimating problem difficulty without ground truth using Large Language Model comparisons

**arXiv**: [2512.14220v1](https://arxiv.org/abs/2512.14220) | [PDF](https://arxiv.org/pdf/2512.14220.pdf)

**作者**: Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**备注**: 19 pages, 10 figures

---

## 💡 一句话要点

**提出基于大语言模型比较的LLM compare方法，以无监督方式估计问题难度，解决分布外问题评估难题。**

**关键词**: `问题难度估计` `大语言模型` `无监督学习` `分布外泛化` `Bradley-Terry模型` `合成数据生成` `课程设计` `模型评估`

## 📋 核心要点

1. 核心问题：现有难度估计方法（如人工校准）依赖真实标签且不可扩展，无法评估分布外问题，限制了合成数据生成。
2. 方法要点：利用大语言模型进行成对难度比较，结合Bradley-Terry模型计算连续分数，实现无监督、模型无关的难度估计。
3. 实验或效果：与人工标注高度相关（Pearson r≥0.80），对噪声鲁棒（性能下降<6%），验证了方法的有效性和稳定性。

## 📝 摘要（中文）

大语言模型（LLMs）微调的进展显著提升了其在基准测试上的性能，这凸显了对更困难合成数据的需求。数据生成流程中的关键步骤是估计问题难度的方法。当前方法（如人工校准或基于性能的评分）由于不可扩展、耗时且依赖真实标签，无法泛化到分布外问题（即当前人类和LLMs无法解决的问题）。因此，我们提出了一种新的问题难度估计方法LLM compare，以解决这些限制。该方法利用LLM进行成对难度比较，然后基于结果计算Bradley-Terry分数。为验证方法，我们首先提出了一个概念框架，将现有方法定位在三个正交平面——构建、规模和依赖性上，识别出评估分布外问题所需占据的象限。LLM compare自然占据了所有理想象限，成为首个连续动态、模型无关且独立于真实标签信息的度量。其次，我们展示了LLM compare与人工标注高度一致：在n=1876时，Pearson相关系数r≥0.80。第三，我们证明LLM compare对幻觉具有鲁棒性，在10%噪声注入下，Pearson相关系数下降小于6%。我们的工作代表了在替代耗时的人工标注和合成数据生成方面的重要一步，并将成为课程设计、模型评估和AI辅助研究构思的重要推动力。

## 🔬 方法详解

LLM compare方法的核心框架基于大语言模型（LLM）的成对比较能力。首先，LLM对问题对进行难度比较，生成相对难度的判断结果；然后，利用Bradley-Terry模型将这些比较结果转化为连续的难度分数。关键技术创新点在于首次实现了完全无监督的难度估计，不依赖真实标签或人类标注，通过LLM的推理能力泛化到未知问题。与现有方法的主要区别在于：现有方法通常基于性能评分（如模型准确率）或人工评估，受限于可解问题和标注成本；而LLM compare通过模型无关的比较机制，能够处理分布外问题，并具有连续动态和可扩展的优势。

## 📊 实验亮点

实验显示LLM compare与人工标注的Pearson相关系数高达0.80以上（n=1876），验证了其有效性；在10%噪声注入下，相关性下降小于6%，证明了方法对幻觉和噪声的强鲁棒性，为无监督难度估计提供了可靠基准。

## 🎯 应用场景

该方法可应用于课程设计中自适应学习路径的生成，通过动态调整问题难度优化教学序列；在模型评估中，为基准测试提供更细粒度的难度分析，辅助性能诊断；在AI辅助研究构思中，帮助生成挑战性合成数据，推动大语言模型的前沿发展。

## 📄 摘要（原文）

> Recent advances in the finetuning of large language models (LLMs) have significantly improved their performance on established benchmarks, emphasizing the need for increasingly difficult, synthetic data. A key step in this data generation pipeline is a method for estimating problem difficulty. Current approaches, such as human calibration or performance-based scoring, fail to generalize to out-of-distribution problems, i.e. problems currently unsolvable by humans and LLMs, because they are not scalable, time-consuming, and ground truth dependent. Therefore, we propose a new method for estimating problem difficulty, LLM compare, that addresses these limitations. An LLM performs pairwise difficulty comparisons, and then Bradley-Terry scores are computed based on the outcomes. To validate our method, we first propose a conceptual framework that positions existing approaches on three orthogonal planes--construction, scale and dependence--identifying which quadrants a measure needs to occupy to score out-of-distribution problems. LLM compare naturally occupies all desirable quadrants as the first measure that is continuous and dynamic, model-agnostic and independent of ground truth information. As a second validation, we show that LLM compare demonstrates strong alignment with human annotations: Pearson $r \geq 0.80$ for $n=1876$. Thirdly, we show that LLM compare is robust to hallucinations, with less than $6\%$ degradation in Pearson correlation for $10\%$ noise injection. Our work represents a significant step towards replacing time-consuming human annotations and synthetic data generation, and will be an important driver for curriculum design, model evaluation, and AI-assisted research ideation.

