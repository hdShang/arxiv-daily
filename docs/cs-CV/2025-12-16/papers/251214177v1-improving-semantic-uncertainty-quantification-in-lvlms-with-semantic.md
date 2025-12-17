---
layout: default
title: Improving Semantic Uncertainty Quantification in LVLMs with Semantic Gaussian Processes
---

# Improving Semantic Uncertainty Quantification in LVLMs with Semantic Gaussian Processes

**arXiv**: [2512.14177v1](https://arxiv.org/abs/2512.14177) | [PDF](https://arxiv.org/pdf/2512.14177.pdf)

**作者**: Joseph Hoche, Andrei Bursuc, David Brellmann, Gilles Louppe, Pavel Izmailov, Angela Yao, Gianni Franchi

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出语义高斯过程不确定性框架，以解决大型视觉语言模型语义不确定性量化中的聚类脆弱性问题。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `语义不确定性量化` `大型视觉语言模型` `高斯过程分类器` `特征谱分析` `贝叶斯框架` `多模态迁移` `模型校准` `嵌入几何结构`

## 📋 核心要点

1. 现有方法依赖外部聚类模型，对措辞变化敏感，易错误分组语义相似答案，导致不确定性估计不可靠。
2. 提出SGPU框架，通过分析答案嵌入的几何结构，避免聚类，使用特征谱和高斯过程分类器量化语义不确定性。
3. 在多个数据集和模型上，SGPU在标定和判别性能方面达到最先进水平，并展示跨模型和模态的迁移能力。

## 📝 摘要（中文）

大型视觉语言模型常产生看似合理但不可靠的输出，因此稳健的不确定性估计至关重要。现有的语义不确定性估计方法依赖外部模型对多个采样响应进行聚类并测量其语义一致性，但这些聚类方法往往脆弱，对细微的措辞变化高度敏感，可能错误地分组或分离语义相似的答案，导致不可靠的不确定性估计。我们提出了语义高斯过程不确定性，这是一个贝叶斯框架，通过分析答案嵌入的几何结构来量化语义不确定性，避免了脆弱的聚类。SGPU将生成的答案映射到密集的语义空间，计算其嵌入的Gram矩阵，并通过特征谱总结其语义配置。这种谱表示随后被输入到高斯过程分类器中，该分类器学习将语义一致性模式映射到预测不确定性，并可在黑盒和白盒设置中应用。在涵盖VQA、图像分类和文本QA的八个数据集上，对六个LLM和LVLM进行测试，SGPU在标定和判别性能方面均达到最先进水平。我们还展示了SGPU能够跨模型和模态迁移，表明其谱表示捕捉了语义不确定性的一般模式。

## 🔬 方法详解

SGPU是一个贝叶斯框架，整体流程包括：将模型生成的多个答案映射到语义空间，计算其嵌入的Gram矩阵，提取特征谱作为语义配置的紧凑表示。关键创新在于避免脆弱的聚类步骤，直接利用嵌入的几何结构，通过高斯过程分类器学习从谱模式到预测不确定性的映射。与现有方法的主要区别在于，它不依赖外部聚类模型，而是基于嵌入的统计特性，提高了鲁棒性和泛化能力，适用于黑盒和白盒设置。

## 📊 实验亮点

在八个数据集和六个模型上，SGPU在标定误差和判别指标方面均达到最先进性能，例如在VQA任务中显著降低错误率，并成功迁移到不同模态任务，验证了其通用性。

## 🎯 应用场景

该研究可应用于需要高可靠性的大型视觉语言模型场景，如自动驾驶中的视觉问答、医疗图像分析、内容审核和智能客服，通过改进不确定性估计，提升模型输出的可信度和安全性。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) often produce plausible but unreliable outputs, making robust uncertainty estimation essential. Recent work on semantic uncertainty estimates relies on external models to cluster multiple sampled responses and measure their semantic consistency. However, these clustering methods are often fragile, highly sensitive to minor phrasing variations, and can incorrectly group or separate semantically similar answers, leading to unreliable uncertainty estimates. We propose Semantic Gaussian Process Uncertainty (SGPU), a Bayesian framework that quantifies semantic uncertainty by analyzing the geometric structure of answer embeddings, avoiding brittle clustering. SGPU maps generated answers into a dense semantic space, computes the Gram matrix of their embeddings, and summarizes their semantic configuration via the eigenspectrum. This spectral representation is then fed into a Gaussian Process Classifier that learns to map patterns of semantic consistency to predictive uncertainty, and that can be applied in both black-box and white-box settings. Across six LLMs and LVLMs on eight datasets spanning VQA, image classification, and textual QA, SGPU consistently achieves state-of-the-art calibration (ECE) and discriminative (AUROC, AUARC) performance. We further show that SGPU transfers across models and modalities, indicating that its spectral representation captures general patterns of semantic uncertainty.

