---
layout: default
title: KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding
---

# KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding

**arXiv**: [2512.14017v1](https://arxiv.org/abs/2512.14017) | [PDF](https://arxiv.org/pdf/2512.14017.pdf)

**作者**: Zongyao Li, Kengo Ishida, Satoshi Yamazaki, Xiaotong Ji, Jianquan Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: WACV2026

**🔗 代码/项目**: [GITHUB](https://github.com/NEC-VID/KFS-Bench)

---

## 💡 一句话要点

**提出KFS-Bench基准和自适应平衡采样方法，以解决长视频问答中关键帧采样评估与性能优化问题。**

**关键词**: `长视频理解` `关键帧采样` `视频问答` `多模态大语言模型` `基准评估` `自适应采样` `场景覆盖` `采样平衡性`

## 📋 核心要点

1. 现有方法仅通过问答准确性间接评估帧选择质量，缺乏直接分析采样策略在多场景长视频中内容捕捉能力的基准。
2. 论文提出KFS-Bench基准，提供多场景真实标注，并设计自适应平衡采样方法，通过问题-视频相关性优化场景覆盖与相似性平衡。
3. 实验表明，自适应平衡采样在关键帧采样和问答性能上均优于现有方法，新设计的采样质量度量与准确性高度相关。

## 📝 摘要（中文）

我们提出了KFS-Bench，这是首个用于长视频问答（QA）中关键帧采样的基准，具有多场景标注功能，能够直接且稳健地评估采样策略。关键帧采样对于高效的长视频理解至关重要。在长视频QA中，选择信息丰富的帧可以使多模态大语言模型（MLLMs）提高准确性和效率。KFS-Bench解决了先前工作仅通过QA准确性间接评估帧选择质量的局限性。通过为每个问题提供所需多个不相交场景的真实标注，KFS-Bench使我们能够直接分析不同采样方法如何在整个长视频中捕捉关键内容。利用KFS-Bench，我们对关键帧采样方法进行了全面研究，发现不仅采样精度，而且场景覆盖率和采样平衡性是影响QA性能的关键因素。基于所有这些因素，我们设计了一种与QA准确性相关的新型采样质量度量。此外，我们开发了一种新颖的关键帧采样方法，利用问题-视频相关性来平衡采样多样性与问题-帧相似性，从而提高相关场景的覆盖率。我们的自适应平衡采样方法在关键帧采样和QA性能方面均实现了卓越表现。该基准可在https://github.com/NEC-VID/KFS-Bench获取。

## 🔬 方法详解

论文的核心方法包括KFS-Bench基准构建和自适应平衡采样方法。整体框架基于长视频问答场景，通过标注多个不相交场景作为真实参考，直接评估采样策略。关键技术创新点在于：1) 设计多场景标注基准，支持直接分析采样内容覆盖；2) 提出新型采样质量度量，综合考虑精度、覆盖率和平衡性；3) 开发自适应平衡采样方法，利用问题-视频相关性动态调整采样，平衡多样性与相似性。与现有方法的主要区别在于，现有工作依赖间接QA评估，而本方法提供直接评估框架，并引入场景覆盖和平衡性作为关键优化因素，从而更全面地提升采样效果。

## 📊 实验亮点

自适应平衡采样方法在KFS-Bench上实现卓越性能，关键帧采样质量显著提升，同时问答准确性得到改善；新设计的采样质量度量与QA准确性高度相关，验证了场景覆盖和平衡性对性能的关键影响。

## 🎯 应用场景

该研究可应用于长视频理解任务，如视频监控分析、教育视频内容提取、影视内容检索等，通过高效关键帧采样提升多模态大语言模型在视频问答中的准确性和效率，具有实际价值于资源受限环境下的实时视频处理。

## 📄 摘要（原文）

> We propose KFS-Bench, the first benchmark for key frame sampling in long video question answering (QA), featuring multi-scene annotations to enable direct and robust evaluation of sampling strategies. Key frame sampling is crucial for efficient long-form video understanding. In long video QA, selecting informative frames enables multimodal large language models (MLLMs) to improve both accuracy and efficiency. KFS-Bench addresses the limitation of prior works that only indirectly assess frame selection quality via QA accuracy. By providing ground-truth annotations of multiple disjoint scenes required per question, KFS-Bench allows us to directly analyze how different sampling approaches capture essential content across an entire long video. Using KFS-Bench, we conduct a comprehensive study of key frame sampling methods and identify that not only sampling precision but also scene coverage and sampling balance are the key factors influencing QA performance. Regarding all the factors, we design a novel sampling quality metric that correlates with QA accuracy. Furthermore, we develop a novel key frame sampling method that leverages question-video relevance to balance sampling diversity against question-frame similarity, thereby improving coverage of relevant scenes. Our adaptively balanced sampling approach achieves superior performance in both key frame sampling and QA performance. The benchmark is available at https://github.com/NEC-VID/KFS-Bench.

