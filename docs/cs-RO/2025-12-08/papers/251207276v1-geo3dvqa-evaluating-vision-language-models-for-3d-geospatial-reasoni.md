---
layout: default
title: Geo3DVQA: Evaluating Vision-Language Models for 3D Geospatial Reasoning from Aerial Imagery
---

# Geo3DVQA: Evaluating Vision-Language Models for 3D Geospatial Reasoning from Aerial Imagery

**arXiv**: [2512.07276v1](https://arxiv.org/abs/2512.07276) | [PDF](https://arxiv.org/pdf/2512.07276.pdf)

**作者**: Mai Tsujimoto, Junjue Wang, Weihao Xuan, Naoto Yokoya

---

## 💡 一句话要点

**提出Geo3DVQA基准，评估仅用RGB遥感图像的视觉语言模型在三维地理空间推理中的性能。**

**关键词**: `三维地理空间推理` `视觉语言模型评估` `遥感图像分析` `基准数据集` `领域适应` `RGB图像处理`

## 📋 核心要点

1. 核心问题：现有方法依赖昂贵传感器，难以整合多3D线索处理多样化查询。
2. 方法要点：构建包含11万问答对的基准，涵盖16个任务类别和三个复杂度级别。
3. 实验或效果：评估10个先进VLM，GPT-4o和Gemini-2.5-Flash准确率低，领域微调Qwen2.5-VL-7B提升至49.6%。

## 📄 摘要（原文）

> Three-dimensional geospatial analysis is critical to applications in urban planning, climate adaptation, and environmental assessment. Current methodologies depend on costly, specialized sensors (e.g., LiDAR and multispectral), which restrict global accessibility. Existing sensor-based and rule-driven methods further struggle with tasks requiring the integration of multiple 3D cues, handling diverse queries, and providing interpretable reasoning. We hereby present Geo3DVQA, a comprehensive benchmark for evaluating vision-language models (VLMs) in height-aware, 3D geospatial reasoning using RGB-only remote sensing imagery. Unlike conventional sensor-based frameworks, Geo3DVQA emphasizes realistic scenarios that integrate elevation, sky view factors, and land cover patterns. The benchmark encompasses 110k curated question-answer pairs spanning 16 task categories across three complexity levels: single-feature inference, multi-feature reasoning, and application-level spatial analysis. The evaluation of ten state-of-the-art VLMs highlights the difficulty of RGB-to-3D reasoning. GPT-4o and Gemini-2.5-Flash achieved only 28.6% and 33.0% accuracy respectively, while domain-specific fine-tuning of Qwen2.5-VL-7B achieved 49.6% (+24.8 points). These results reveal both the limitations of current VLMs and the effectiveness of domain adaptation. Geo3DVQA introduces new challenge frontiers for scalable, accessible, and holistic 3D geospatial analysis. The dataset and code will be released upon publication at https://github.com/mm1129/Geo3DVQA.

