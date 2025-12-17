---
layout: default
title: SELECT: Detecting Label Errors in Real-world Scene Text Data
---

# SELECT: Detecting Label Errors in Real-world Scene Text Data

**arXiv**: [2512.14050v1](https://arxiv.org/abs/2512.14050) | [PDF](https://arxiv.org/pdf/2512.14050.pdf)

**作者**: Wenjun Liu, Qian Wu, Yifeng Hu, Yuke Li

**分类**: cs.CV

**发布日期**: 2025-12-16

**DOI**: [10.1145/3743093.3771031](https://doi.org/10.1145/3743093.3771031)

---

## 💡 一句话要点

**提出SELECT方法，利用多模态训练检测真实场景文本数据集中的标签错误，解决变长标签序列和字符级错误问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `场景文本识别` `标签错误检测` `多模态训练` `字符级分词器` `序列标签损坏` `视觉相似性` `真实世界数据集` `变长序列处理`

## 📋 核心要点

1. 现有方法难以处理真实场景文本数据中的变长标签序列、标签错位和字符级错误，导致标签错误检测不准确。
2. SELECT采用多模态训练，结合图像-文本编码器和字符级分词器，并引入SSLC过程模拟真实错误，提升检测鲁棒性。
3. 实验显示SELECT在标签错误检测和STR准确性上优于现有方法，验证了其在真实数据集上的实用性和有效性。

## 📝 摘要（中文）

我们介绍了SELECT（Scene tExt Label Errors deteCTion），一种新颖的方法，利用多模态训练来检测真实场景文本数据集中的标签错误。通过使用图像-文本编码器和字符级分词器，SELECT解决了变长序列标签、标签序列错位和字符级错误的问题，在准确性和实用性上优于现有方法。此外，我们引入了基于相似性的序列标签损坏（SSLC）过程，该过程在训练期间有意向训练标签中引入错误，以模拟真实世界的错误场景。SSLC不仅可能导致序列长度变化，还在损坏过程中考虑了字符之间的视觉相似性。我们的方法是首个成功检测真实场景文本数据集中标签错误并考虑变长标签的方法。实验结果表明，SELECT在检测标签错误和提高真实世界文本数据集上的场景文本识别（STR）准确性方面具有有效性，展示了其实用价值。

## 🔬 方法详解

SELECT的整体框架基于多模态训练，使用图像-文本编码器提取视觉和文本特征，字符级分词器处理变长序列。关键技术创新包括SSLC过程，该过程在训练中引入基于视觉相似性的标签错误，模拟真实场景的字符替换和序列长度变化。与现有方法的主要区别在于，SELECT是首个专门针对真实场景文本数据中变长标签序列设计的错误检测方法，通过多模态融合和SSLC增强了模型对复杂错误的处理能力。

## 📊 实验亮点

实验结果表明，SELECT在真实场景文本数据集上显著提高了标签错误检测的准确性，并改善了场景文本识别（STR）模型的性能，优于现有基准方法，展示了其在实际应用中的优势。

## 🎯 应用场景

该研究可应用于自动驾驶、文档数字化、智能监控等领域的场景文本识别系统，通过检测和纠正标签错误，提升数据质量和模型性能，具有实际部署价值。

## 📄 摘要（原文）

> We introduce SELECT (Scene tExt Label Errors deteCTion), a novel approach that leverages multi-modal training to detect label errors in real-world scene text datasets. Utilizing an image-text encoder and a character-level tokenizer, SELECT addresses the issues of variable-length sequence labels, label sequence misalignment, and character-level errors, outperforming existing methods in accuracy and practical utility. In addition, we introduce Similarity-based Sequence Label Corruption (SSLC), a process that intentionally introduces errors into the training labels to mimic real-world error scenarios during training. SSLC not only can cause a change in the sequence length but also takes into account the visual similarity between characters during corruption. Our method is the first to detect label errors in real-world scene text datasets successfully accounting for variable-length labels. Experimental results demonstrate the effectiveness of SELECT in detecting label errors and improving STR accuracy on real-world text datasets, showcasing its practical utility.

