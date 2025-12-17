---
layout: default
title: Where on Earth? A Vision-Language Benchmark for Probing Model Geolocation Skills Across Scales
---

# Where on Earth? A Vision-Language Benchmark for Probing Model Geolocation Skills Across Scales

**arXiv**: [2510.10880v1](https://arxiv.org/abs/2510.10880) | [PDF](https://arxiv.org/pdf/2510.10880.pdf)

**作者**: Zhaofang Qian, Hardy Chen, Zeyu Wang, Li Zhang, Zijun Wang, Xiaoke Huang, Hui Liu, Xianfeng Tang, Zeyu Zheng, Haoqin Tu, Cihang Xie, Yuyin Zhou

---

## 💡 一句话要点

**提出EarthWhere基准以评估视觉语言模型在开放世界图像地理定位能力**

**关键词**: `图像地理定位` `视觉语言模型` `基准评估` `多尺度推理` `区域偏见` `开放世界任务`

## 📋 核心要点

1. 核心问题：视觉语言模型在开放世界图像地理定位能力未全面评估，任务具挑战性和现实需求。
2. 方法要点：构建EarthWhere基准，包含多尺度地理定位任务，并引入推理链评分和Shapley重加权思考分数。
3. 实验或效果：评估13个先进模型，Gemini-2.5-Pro平均准确率最高，模型存在区域偏见和推理限制。

## 📄 摘要（原文）

> Vision-language models (VLMs) have advanced rapidly, yet their capacity for
> image-grounded geolocation in open-world conditions, a task that is challenging
> and of demand in real life, has not been comprehensively evaluated. We present
> EarthWhere, a comprehensive benchmark for VLM image geolocation that evaluates
> visual recognition, step-by-step reasoning, and evidence use. EarthWhere
> comprises 810 globally distributed images across two complementary geolocation
> scales: WhereCountry (i.e., 500 multiple-choice question-answering, with
> country-level answer and panoramas) and WhereStreet (i.e., 310 fine-grained
> street-level identification tasks requiring multi-step reasoning with optional
> web search). For evaluation, we adopt the final-prediction metrics: location
> accuracies within k km (Acc@k) for coordinates and hierarchical path scores for
> textual localization. Beyond this, we propose to explicitly score intermediate
> reasoning chains using human-verified key visual clues and a Shapley-reweighted
> thinking score that attributes credit to each clue's marginal contribution. We
> benchmark 13 state-of-the-art VLMs with web searching tools on our EarthWhere
> and report different types of final answer accuracies as well as the calibrated
> model thinking scores. Overall, Gemini-2.5-Pro achieves the best average
> accuracy at 56.32%, while the strongest open-weight model, GLM-4.5V, reaches
> 34.71%. We reveal that web search and reasoning do not guarantee improved
> performance when visual clues are limited, and models exhibit regional biases,
> achieving up to 42.7% higher scores in certain areas than others. These
> findings highlight not only the promise but also the persistent challenges of
> models to mitigate bias and achieve robust, fine-grained localization. We
> open-source our benchmark at https://github.com/UCSC-VLAA/EarthWhere.

