---
layout: default
title: RosettaSpeech: Zero-Shot Speech-to-Speech Translation from Monolingual Data
---

# RosettaSpeech: Zero-Shot Speech-to-Speech Translation from Monolingual Data

**arXiv**: [2511.20974v1](https://arxiv.org/abs/2511.20974) | [PDF](https://arxiv.org/pdf/2511.20974.pdf)

**作者**: Zhisheng Zheng, Xiaohang Sun, Tuan Dinh, Abhishek Yanamandra, Abhinav Jain, Zhu Liu, Sunil Hadap, Vimal Bhat, Manoj Aggarwal, Gerard Medioni, David Harwath

---

## 💡 一句话要点

**提出RosettaSpeech框架，利用单语数据和机器翻译实现零样本语音到语音翻译。**

**关键词**: `语音到语音翻译` `零样本学习` `单语数据训练` `机器翻译监督` `端到端模型`

## 📋 核心要点

1. 核心问题：平行语音语料稀缺，阻碍语音到语音翻译发展。
2. 方法要点：训练时使用文本作为桥梁，推理时端到端直接翻译语音。
3. 实验效果：在CVSS-C测试集上，德语到英语ASR-BLEU达25.17，性能领先。

## 📄 摘要（原文）

> The scarcity of parallel speech corpora critically hampers speech-to-speech translation (S2ST), often forcing reliance on complex, multi-stage pipelines. This paper introduces RosettaSpeech, a novel and simplified framework for zero-shot S2ST that is trained on monolingual speech-text data augmented by machine translation supervision. While our method leverages the linguistic knowledge inherent in text-based NMT models, it strictly eliminates the need for parallel speech-to-speech pairs. Our model uniquely uses text as an intermediate bridge during training but functions as a direct, end-to-end speech-to-speech model at inference. This streamlined approach achieves state-of-the-art results on standard benchmarks. For instance, on the CVSS-C test set, RosettaSpeech outperforms leading systems, achieving an ASR-BLEU score of 25.17 for German-to-English and 29.86 for Spanish-to-English-relative gains of over 27% and 14%, respectively. Furthermore, we demonstrate that a single model can deliver strong many-to-one translation performance (FR/ES/DE -> EN). We also provide a foundational analysis of how training data scaling impacts model performance. By prioritizing reliance on abundant parallel text rather than difficult-to-acquire parallel speech, RosettaSpeech offers a scalable path to creating high-quality, speaker-preserving S2ST for a much broader array of languages.

